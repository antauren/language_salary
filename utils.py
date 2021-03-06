import requests

from terminaltables import SingleTable

from statistics import mean

from tqdm import tqdm


def make_table(data: list, title: str) -> str:
    header = ['language', 'vacancies_found', 'vacancies_processed', 'avarage_salary']
    header_rus = ['Язык программирования', 'Найдено вакансий', 'Обработано вакансий', 'Средняя зарплата']

    table = [header_rus]

    for val_dict in data:
        row = [val_dict[col_name] for col_name in header]
        table.append(row)

    table_instance = SingleTable(table, title)
    for index in range(1, len(header)):
        table_instance.justify_columns[index] = 'right'

    return table_instance.table


def get_predict_salary(salary_from, salary_to):
    if (salary_from is None) and (salary_to is None):
        return None

    elif salary_from is None:
        return salary_to * 0.8

    elif salary_to is None:
        return salary_from * 1.2

    else:
        return mean([salary_from, salary_to])


def get_stat_dict(salary_list) -> dict:
    vacancies_found = len(salary_list)

    salary_list_filtered = [salary for salary in salary_list if salary is not None]

    vacancies_processed = len(salary_list_filtered)

    return {'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_processed,
            'avarage_salary': int(mean(salary_list_filtered))

            }


def get_languages_stat_list(languages, fetch_records, get_predict_rub_salary, desc=''):
    languages_stat_list = []

    languages = tqdm(languages, desc=desc)

    for language in languages:

        try:
            vacancies = list(fetch_records(language))

        except requests.exceptions.HTTPError as error:
            print("Can't get data from server:\n{}".format(error))
            continue

        salary_list = list(map(get_predict_rub_salary, vacancies))

        stat = get_stat_dict(salary_list)
        stat['language'] = language

        languages_stat_list.append(stat)
    return languages_stat_list
