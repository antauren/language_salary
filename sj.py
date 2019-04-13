from functools import partial

import requests

from utils import make_table, get_predict_salary, get_languages_stat_list


def get_stat_table_SJ(languages: list, params: dict, headers: dict, title='SuperJob') -> str:
    p_fetch_records_sj = partial(fetch_records_sj, params=params, headers=headers)

    languages_stat_list = get_languages_stat_list(languages, p_fetch_records_sj, get_predict_rub_salary_sj,
                                                  desc=fetch_records_sj.__name__)
    table = make_table(languages_stat_list, title)

    return table


def get_predict_rub_salary_sj(vacancy):
    if vacancy['currency'] != 'rub':
        return None

    payment_from, payment_to = vacancy['payment_from'], vacancy['payment_to']

    payment_from, payment_to = map(lambda payment: None if not payment else payment, [payment_from, payment_to])

    return get_predict_salary(payment_from, payment_to)


def fetch_records_sj(text: str, params: dict, headers: dict):
    path = 'https://api.superjob.ru/2.0/vacancies/'

    params = params.copy()

    params['keywords'] = text

    page = 0
    more = True

    while more:
        params['page'] = page

        response = requests.get(path, headers=headers, params=params)
        if not response.ok:
            continue

        page_data = response.json()

        more = page_data['more']
        page += 1

        yield from page_data['objects']


if __name__ == '__main__':
    pass
