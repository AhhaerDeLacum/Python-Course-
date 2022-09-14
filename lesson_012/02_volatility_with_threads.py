# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
