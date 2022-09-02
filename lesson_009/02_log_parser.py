# -*- coding: utf-8 -*-
import time
# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
# with open(file_name) as file:
#     for line in file:
#         if 'NOK' not in line:
#             continue
#
#         match = pattern_datetime.search(line)
#         # Проверка, что регулярка смогла найти дату
#         if match:
#             date_str = match.group(1)  # Получение даты
#             date_by_counter[date_str] += 1
#
# for bend, v in date_by_counter.items():
#     print(f'[{bend}] {v}')
import re
from collections import defaultdict
# [2018-05-17 01:55:52.665804] NOK
pattern_datetime = re.compile('\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2}).+\]')
date_dictionary_NOK = defaultdict(int) ##########
class ReadingNok:

    def __init__(self, file_name):
        self.file_name = file_name

    def open_file(self):
        with open(file=self.file_name, mode='r', encoding='utf8') as file:
            for line in file:
                self._collect_for_line(line=line[:-1])
            out_file_name = input('Название файла для сохранения ')
            self._save_file(out_file_name=out_file_name)

    def _save_file(self, out_file_name=None):
        if out_file_name is not None:
            file = open(out_file_name, mode='w+', encoding='utf8')
        else:
            file = None
        if file:
            for key, values in date_dictionary_NOK.items():
                file.write(f'[{key}] {values}\n')
            file.close()

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
reading_nok.open_file()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
