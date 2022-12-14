# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от средней цены за торговую сессию:
#   средняя цена = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / средняя цена) * 100%
# Например для бумаги №1:
#   average_price = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / average_price) * 100 = 8.7%
# Для бумаги №2:
#   average_price = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / average_price) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base_source/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
# class <Название класса>:
#
#     def __init__(self, <параметры>):
#         <сохранение параметров>
#
#     def run(self):
#         <обработка данных>
import os
import time
from collections import defaultdict

class FilesOpenForCalculatingVolatility():

    def __init__(self, path_name):
        self.file_name = None
        self.path_name = os.path.normpath(path_name)
        self.full_file_path = None
        self.max_price = None
        self.min_price = None
        self.average_price = 0 ######
        self.volatility = 0 ########
        self.list_volatility = []
        self.list_zero_volatility = []

    def run(self):
        try:
            self.opendir()
            self.list_volatility.sort()
            #self.list_zero_volatility.sort()
        except Exception as exc:
            print(exc)

    def opendir(self):
        if self.path_name:
            for dirpath, dirnames, filenames in os.walk(self.path_name):
                #print(dirpath, dirnames, filenames) &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
                for file in filenames:
                    self.file = file # не уверен в надобности
                    self.full_file_path = os.path.join(dirpath, self.file)
                    self._open()



    def _open(self):
        #print('###' * 10)
        self.ticker_dict = defaultdict(int) ###########
        is_it_first_line = True
        with open(self.full_file_path, mode='r', encoding='utf8') as file:
            for line in file:
                if is_it_first_line:
                    is_it_first_line = False
                else:
                    line = line[:-1]
                    #print(line) #######################
                    self.SECID, TRADETIME, PRICE, QUANTITY = line.split(',')
                    self._identification_min_and_max(PRICE)
            #print('open _calculating') &&&&&&&&&&&
            #time.sleep(2) &&&&&&&&&&&&&&&&&&&&&
            self._calculating()



    # Например для бумаги №1:
    #   average_price = (12 + 11) / 2 = 11.5
    #   volatility = ((12 - 11) / average_price) * 100 = 8.7%
    def _calculating(self):
        self.average_price = (self.min_price + self.max_price) / 2
        self.volatility = ((self.max_price - self.min_price) / self.average_price) * 100
        self.volatility = round(self.volatility, 2)
        # print(self.min_price)
        # print(self.max_price)
        #print(f'{self.volatility}%') %%%%%%%%%%%%%%%%%%%%%%%%
        # time.sleep(2)
        if self.volatility == 0:
            self.list_zero_volatility.append(self.SECID)
        else:
            self.list_volatility.append((self.volatility, self.SECID))
        self.max_price = None
        self.min_price = None
        #print(self.list_volatility) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        # print(self.min_price)
        # print(self.max_price)
        # print(f'{self.volatility}%')

    def _identification_min_and_max(self, PRICE):
        PRICE = float(PRICE)
        if self.min_price is None or self.max_price is None:
            self.min_price = PRICE
            self.max_price = PRICE
        elif self.min_price > PRICE:
            self.min_price = PRICE
        elif self.max_price < PRICE:
            self.max_price = PRICE
        #print(PRICE) #####################

calculating_files = FilesOpenForCalculatingVolatility(path_name="trades")
calculating_files.run()
print('Максимальная волатильность:')
for max_v in calculating_files.list_volatility[:-4:-1]:
    print(max_v)
print('Минимальная волатильность:')
for min_v in calculating_files.list_volatility[2::-1]:
    print(min_v)
print('Нулевая волатильность:')

result = [x for x in calculating_files.list_zero_volatility]
print(result)
# for zero_v in calculating_files.list_zero_volatility:
#     print(zero_v)