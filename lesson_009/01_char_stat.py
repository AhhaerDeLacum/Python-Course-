# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.
from pprint import pprint
class Counting:
    analize_count = 1 ###########################
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.all_symbols = 0
    #обработать файл
    #затем вычисления ( подсчет )
    #вывод
    def open_file(self):
        self.sequence = ' ' * self.analize_count ##################
        with open(self.file_name, 'r',) as file:
            for line in file:
                #pprint(line[:-1])
                self._collect_for_line(line=line[:-1]) #Чтобы не учитывался символ перехода на новую строку line[:-1]

    def _collect_for_line(self, line):
        i = 0
        for char in line:
            if char.isalpha():
                self.all_symbols += 1
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1
                i += 1

    def out_file(self, sort_type):
        txt_border = '+---------+----------+'
        txt_data = '|  буква  | частота  |'
        txt_conclusion = 'Итого'
        print(f'{txt_border}')
        print(txt_data)
        print(f'{txt_border}')
        self._types_of_sorting(sort_type=sort_type)
        # for symbol, amount in sorted(self.stat.items(), key=lambda item: item[1]):
        #     print('|{symbol:^9}|{amount:^10}|'.format(symbol=symbol, amount=amount))
        print(txt_border)
        print(f'|{txt_conclusion:^9}|{self.all_symbols:^10}|')
        print(txt_border)
        # pprint(self.stat)
        # #pprint(sorted(self.stat))

    def _types_of_sorting(self, sort_type):
        '''Сортировка разных видов:
        - по частоте по возрастанию
        - по алфавиту по возрастанию
        - по алфавиту по убыванию'''
        if sort_type == 1:
            for symbol, amount in sorted(self.stat.items(), key=lambda item: item[1]):
                print('|{symbol:^9}|{amount:^10}|'.format(symbol=symbol, amount=amount))
        elif sort_type == 2:
            for symbol, amount in sorted(self.stat.items()):
                print('|{symbol:^9}|{amount:^10}|'.format(symbol=symbol, amount=amount))
        elif sort_type == 3:
            for symbol, amount in sorted(self.stat.items(), reverse=True):
                print('|{symbol:^9}|{amount:^10}|'.format(symbol=symbol, amount=amount))
        else:
            print('Неверный номер. Сортировка есть трех видов 1 до 3')
# >>> dict(sorted(x.items(), key=lambda item: item[1]))
# {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}
# dict1 = {1: 1, 2: 9, 3: 4}
# sorted_tuples = sorted(dict1.items(), key=lambda item: item[1])
# print(sorted_tuples)  # [(1, 1), (3, 4), (2, 9)]
# sorted_dict = {k: v for k, v in sorted_tuples}


counting = Counting(file_name='voyna-i-mir.txt')
counting.open_file()
counting.out_file(sort_type=1)
counting.out_file(sort_type=2)
counting.out_file(sort_type=3)
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

