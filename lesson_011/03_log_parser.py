# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234

import re
from collections import defaultdict
# [2018-05-17 01:55:52.665804] NOK
pattern_datetime = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')
date_dictionary_NOK = defaultdict(int) ##########
class ReadingNok:

    def __init__(self, file_name):
        self.file_name = file_name
        self.i = 0
        self.n = 0
        self.counter_for_dict = 0
        self.list = []

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        if self.n == 0:
            self.n += 1
            self.open_file()
        if self.n == 1:
            for key, values in date_dictionary_NOK.items():
                self.list.append(key)
                self.n += 1
        while self.i < self.counter_for_dict:
            self.key = self.list[self.i]
            self.values = date_dictionary_NOK[self.list[self.i]]
            self.i += 1
            return self.key, self.values
        else:
            raise StopIteration()
            #return self.list[self.i], date_dictionary_NOK[self.list[self.i]]

            #return date_dictionary_NOK([self.i])

            # for key, values in date_dictionary_NOK.items():
            #     return key, values
    #def return_key_values(self):


    def open_file(self):
        with open(file=self.file_name, mode='r', encoding='utf8') as file:
            for line in file:
                #self.n += 1
                self._collect_for_line(line=line[:-1])
            self.counter_for_dict = len(date_dictionary_NOK)
            # out_file_name = input('Название файла для сохранения ')
            #self._save_file()

    # def save_file(self):
    #     for key, values in date_dictionary_NOK.items():
    #         return key, values
            #print(f'[{key}] {values}\n')

    def _collect_for_line(self, line):
        event_nok = 'NOK'
        if event_nok in line:
            match = pattern_datetime.search(line)
            if match:
                date_str = match.group(1)
                date_dictionary_NOK[date_str] += 1

            # for bend, v in date_dictionary_NOK.items():
            #     print(f'[{bend}] {v}')


reading_nok = ReadingNok(file_name='events.txt')
#reading_nok.open_file()
#grouped_events = <создание итератора/генератора>
for group_time, event_count in reading_nok:
    print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234