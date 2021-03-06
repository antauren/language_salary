# Прикидываем зарплату программиста в Москве

Скрипт скачивает вакансии разработчиков с HeadHunter и SuperJob за последнюю неделю, считет среднюю зарплату для каждого языка программирования, и выводит эти данные в виде таблицы

| Язык программирования | Вакансий найдено | Вакансий обработано | Средняя зарплата |
|:-----------------------|-----------------:|--------------------:|-----------------:|
| python                | 10               | 7                   | 90714            |
| c                     | 19               | 9                   | 103866           |
| c#                    | 38               | 15                  | 95200            |
| c++                   | 26               | 17                  | 89585            |
| java                  | 36               | 12                  | 101791           |
| js                    | 39               | 20                  | 100400           |
| ruby                  | 3                | 3                   | 166000           |
| go                    | 4                | 3                   | 120833           |
| 1с                    | 113              | 64                  | 116129           |



### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```


#### Нужно авторизоваться
HeadHunter этого не требует, а вот SuperJob не отдаст данные без авторизации: 
1. Получите ключ к API SuperJob:  https://api.superjob.ru/  
  
2. Создайте в корневой папке файл ```.env``` и пропишите в нем свои данные следующим образом:  
     ```
     secret_key=v3.r.123456789.2e6b1b9a274695f2
     ``` 
     


### Как запустить
```
python language_salary.py
```



### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).