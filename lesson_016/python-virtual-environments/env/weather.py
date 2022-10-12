# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погода
# Из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}
import codecs
import re
import sys
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import lxml
###############################response = requests.get("https://yandex.ru/pogoda/")
# print(response.text.encode(encoding='utf-8'))
# with open("index.html", 'w', encoding='utf-8', errors='ignore') as file:
#     file.write(response.text)

#
# # print(list_of_date)
# # print(list_of_weather)
# # print(list_of_temperature_max)
# # print(list_of_temperature_min)
# for tag in list_of_date:
#     print(tag.text)

'''for i in range(len(a)):
    aria_label = a[i]
    print(aria_label['aria-label'])
    if 'aria-label' in aria_label:
        print(aria_label, '\n')'''
# all_tabs = soup.find_all(class_="link link_theme_normal text forecast-briefly__day-link i-bem link_js_inited")
# for i in all_tabs:
#     print(i)
# soup.p
# # <p class="title"><b>The Dormouse's story</b></p>
# aria-label="вчера, 5 октября, небольшой дождь, днём 8°, ночью 6°"


# try:
#     all_tabs = soup.find_all('a')
#     for i in all_tabs:
#         print(i)
#
#     soup.get_text()
#     u'\nI linked to example.com\n'
#     print(soup.i.get_text())
#     u'example.com'
# except BaseException as exc:
#     print(exc)
    # i['aria-label']
# u'title'
# if response.status_code == 200:
#     html_doc = BeautifulSoup(response.text.encode(encoding='utf-8'), features='html.parser')
# list_of_date = soup.find_all('time', {'class': "time forecast-briefly__date"})#html_doc.find_all('a', {'class': 'link link_theme_normal text forecast-briefly__day-link i-bem link_js_inited'})
# list_of_weather = soup.find_all('div', {'class': 'forecast-briefly__condition'})
# list_of_temperature_max = soup.find_all('span', {'class': 'temp__value temp__value_with-unit'})
# list_of_temperature_min = soup.find_all('span', {'class': 'temp__value temp__value_with-unit'})
#
#
# print(list_of_date)
# print(list_of_weather)
# print(list_of_temperature_max)
# print(list_of_temperature_min)
# for tag in list_of_date:
#     print(tag.text)
    # for names, values in zip(list_of_names, list_of_values):
    #     print(names.text, values.text)
    # for link in html_doc.find_all('a'):
    #     print(link.get('href'))
    # http://example.com/elsie
    # http://example.com/lacie
    # http://example.com/tillie
# Чтобы узнать, какие теги нам нужны, нужно проанализировать саму страницу
# Для этого можно открыть её в браузере и посмотреть код всей страницы или нужного элемента.

# В нашем случае это теги 'span' и 'a' c атрибутами 'class:...'
# Пример того, как это выглит внутри документа:
# <a class="home-link home-link_black_yes inline-stocks__link" href="https://news.yandex.ru/quotes/2002.html"
# data-statlog="news_rates_manual.id2002" data-statlog-showed="1">USD&nbsp;MOEX</a>
# with open('index.html', 'r', encoding='utf-8', errors='ignore') as file:
#     src = file.read()
# soup = BeautifulSoup(response.text.encode(encoding='utf-8'), features='html.parser') # BeautifulSoup(response.text.encode(encoding='utf-8'), features='html.parser')
# list_of_date = soup.find_all('div', {'aria-hidden': "true"})
# print(list_of_date)

# def class_no_id(tag):
#     return tag.has_attr('aria-hidden') and not tag.has_attr('class')
# for tag in soup.find_all(class_no_id):
#     print(tag.text)
# for i in list_of_date:
#     print(i)

class Weather:
    def __init__(self):
        self.month = None
        self.url = "https://yandex.ru/pogoda/"
        self.dict_of_weather = {
            'day_of_week': '',
            'day_with_month': '',
            'weather': '',
            'max_temperature': '',
            'min_temperature': '',
            'min_temperature': '',
            'day': '',
            'month': '',
        }
        self.weather_per_days_dict = {}
        self.pattern_day_with_month = r'[0-9]{1,2} [А-я]{3}'
        self.pattern_weather = r'\d[А-я]{1,12} {0,1}[А-я]{0,12} {0,1}[А-я]{0,12}'
        self.pattern_max_and_min_temperature = r'[^\w]{1}\d{1,2}'
        self.pattern_min_temperature = r''
        self.run()

    def run(self):
        self.open()
        # print(self.weather_per_days_dict)
        return self.weather_per_days_dict

    def open(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            src = response.text.encode(encoding='utf-8')
            ''' Можно расскомментить и спарсить данные и  сохранить сначала в файл, а потом открыть его через файл
            
            # with open("index.html", 'w', encoding='utf-8', errors='ignore') as file:
            #     file.write(response.text)
            
            with open('index.html', 'r', encoding='utf-8', errors='ignore') as file:
                src = file.read()
            
            '''
            soup = BeautifulSoup(src, 'html.parser')
            list_of_date = soup.find_all('time', {'class': "time forecast-briefly__date"})  # html_doc.find_all('a', {'class': 'link link_theme_normal text forecast-briefly__day-link i-bem link_js_inited'})
            list_of_weather = soup.find_all('div', {'class': 'forecast-briefly__condition'})
            list_of_temperature_max = soup.find_all('span', {'class': 'temp__value temp__value_with-unit'})
            list_of_temperature_min = soup.find_all('span', {'class': 'temp__value temp__value_with-unit'})

            counter = 0

        def tag_has_attr_aria_hidden(tag):
            return tag.has_attr('aria-hidden') and not tag.has_attr('class')

        for tag in soup.find_all(tag_has_attr_aria_hidden):
            if counter != 0:
                ##########################################################   print(tag.text)
                # print(tag.text.split())
                dict_of_weather = {
                    'day_of_week': '',
                    'day': '',
                    'month': '',
                    'weather': '',
                    'max_temperature': '',
                    'min_temperature': '',
                }
                """Переменные для изменений значений tag.text 'Вчера' и 'Сегодня'
                """
                now = datetime.now()
                list_day_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
                yesterday = now.weekday() - 1
                today = now.weekday()
                if 'Вчера' in tag.text:
                    day_of_week = list_day_of_week[yesterday]

                    day, month = re.search(self.pattern_day_with_month, tag.text).group().split()
                    max_temperature, min_temperature = (re.findall(self.pattern_max_and_min_temperature, tag.text))
                    weather = re.search(self.pattern_weather, tag.text).group()[1:]
                elif 'Сегодня' in tag.text:
                    day_of_week = list_day_of_week[today]
                    weather = re.findall(self.pattern_weather, tag.text)[1][1:]

                    day, month = re.search(self.pattern_day_with_month, tag.text).group().split()
                    max_temperature, min_temperature = (re.findall(self.pattern_max_and_min_temperature, tag.text))
                else:
                    """Пн-Вс из двух букв"""
                    day_of_week = (tag.text[:2])

                    day, month = re.search(self.pattern_day_with_month, tag.text).group().split()
                    max_temperature, min_temperature = (re.findall(self.pattern_max_and_min_temperature, tag.text))
                    weather = re.search(self.pattern_weather, tag.text).group()[1:]
                """Может надо преобразовать мин и макс температуру в int() """

                dict_of_weather['day_of_week'] = day_of_week
                dict_of_weather['day'] = day
                dict_of_weather['month'] = month #########Почему-то ошибка с принтом дей и монтх
                dict_of_weather['max_temperature'] = max_temperature
                dict_of_weather['min_temperature'] = min_temperature
                dict_of_weather['weather'] = weather

                # print(day_of_week)
                # print(day)
                # print(month)
                # print(max_temperature, min_temperature)
                # print(weather)
                # print(dict_of_weather)
                self.weather_per_days_dict[day] = dict_of_weather
            counter = 1

    def probe(self):

        pass


    def parsing(self):
        pass


if __name__ == "__main__":
    weather = Weather()
    weather.run()