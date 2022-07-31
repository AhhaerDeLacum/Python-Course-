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
            if char.isalpha():                                  # {л:1, б:3}                                                              #  0     1
                if char in self.stat:
                    self.stat[char] += 1
                else:
                    self.stat[char] = 1
                i += 1

    def out_file(self):
        txt_border = '+---------+----------+'
        txt_data = '|  буква  | частота  |'
        print(f'{txt_border}')
        print(txt_data)
        for symbol, amount in self.stat.items():
            print('|{symbol:^9}|{amount:^10}|'.format(symbol=symbol, amount=amount))
        print(txt_border)
        #pprint(self.stat)

counting = Counting(file_name='voyna-i-mir.txt')
counting.open_file()
counting.out_file()
# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828

