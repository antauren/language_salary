from dotenv import dotenv_values

from sj import get_stat_table_SJ
from hh import get_stat_table_HH

if __name__ == '__main__':
    languages = ['c', 'python', 'c#', 'c++', 'java', 'js', 'ruby', 'go', '1с']

    headers_sj = {'X-Api-App-Id': dotenv_values()['secret_key']}
    params_sj = {
        'count': 100,
        'town': 4,  # Москва
        'catalogues': 48,
        'period': 7
    }

    # ---------------------------------------------------------------------

    params_hh = {
        'area': 1,  # Mосква
        'only_with_salary': True,  # не брать те вакансии, где нет данных о зарплате
        'per_page': 100,

        'period': 7,
        'premium': True
    }

    # ---------------------------------------------------------------------

    table_sj = get_stat_table_SJ(languages, params_sj, headers_sj, 'SuperJob Moscow')
    table_hh = get_stat_table_HH(languages, params_hh, 'HeadHunter Moscow')  #

    print(table_sj)
    print(table_hh)
