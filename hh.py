from functools import partial

import requests
from itertools import count

from tqdm import tqdm

from utils import make_table, get_stat_dict, get_predict_salary, get_languages_stat_list


def get_stat_table_HH(languages: list, params: dict, title='HeadHunter') -> str:
    p_fetch_records_sj = partial(fetch_records_hh, params=params)

    languages_stat_list = get_languages_stat_list(languages, p_fetch_records_sj, get_predict_rub_salary_hh,
                                                  desc=fetch_records_hh.__name__)
    table = make_table(languages_stat_list, title)

    return table


def get_predict_rub_salary_hh(vacancy_dict):
    if vacancy_dict is None:
        return None

    salary_dict = vacancy_dict['salary']

    if salary_dict['currency'] != 'RUR':
        return None

    return get_predict_salary(salary_dict['from'], salary_dict['from'])


def fetch_records_hh(text: str, params: dict):
    params = params.copy()

    params['text'] = text

    path = 'https://api.hh.ru/vacancies'

    pages = 0

    for page in count(start=0):

        if page > pages:
            break

        params['page'] = page

        response = requests.get(path, params=params)
        if not response.ok:
            response.raise_for_status()
            continue

        page_data = response.json()

        pages = page_data['pages']

        yield from page_data['items']


if __name__ == '__main__':
    pass
