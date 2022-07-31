# from pprint import pprint
#
#
# file_name = 'pushkin.txt'
# file = open(file_name, mode='r', encoding='utf8')
# file_content = file.read()
# file.close()
# pprint(file_content)
# string_ = '123456789'
# print(string_[:-1])
_dict = {'k':21, 'b':14, 'h':9, }
while True:
    print(_dict['k'])
    print(_dict['h'])
    break
    # {л:1, б:3}                                                              #  0     1
    # if char in _dict:
    #     self.stat[char] += 1
    # else:
    #     self.stat = {char: 1}
    # i += 1
# txt = 'строка'
# print(f'{txt:*^30}')
# # очень похож на .format() но только сначала вычисляется пайтон выражение, а потом применяется форматирование
# # тут txt - это имя переменной
# # можно так: писать код внутри строки :( получается ужасно, на мой вкус
# var_1 = 34
# print(f'Удвоенное значение переменной - {var_1 * 2:10d}')
# # можно даже делать операции индексирования
# my_list = [1, 2, 3, 4]
# print(f'Третий элемент списка - {my_list[2]:10d}')
# my_dict = {'a': 1, 'b': 2}
# print(f"Значение словаря - {my_dict['a']:10d}")
# # или вызывать функции... но лучше так не делать :)
# print(len('|    А    |   77777  |'))
# import time
# time.gmtime(secs)  # вернет тьюпл со временем https://docs.python.org/3/library/time.html#time.struct_time
import time
time.gmtime(secs=12314121412)