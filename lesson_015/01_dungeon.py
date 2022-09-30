# -*- coding: utf-8 -*-

# С помощью JSON файла rpg.json задана "карта" подземелья.
# Подземелье было выкопано монстрами и они всё ещё скрываются где-то в его глубинах,
# планируя набеги на близлежащие поселения.
# Само подземелье состоит из двух главных разветвлений и нескольких развилок,
# и лишь один из путей приведёт вас к главному Боссу
# и позволит предотвратить набеги и спасти мирных жителей.

# Напишите игру, в которой пользователь, с помощью консоли,
# сможет:
# 1) исследовать это подземелье:
#   -- передвижение должно осуществляться присваиванием переменной и только в одну сторону
#   -- перемещаясь из одной локации в другую, пользователь теряет время, указанное в конце названия каждой локации
# Так, перейдя в локацию Location_1_tm500 - вам необходимо будет списать со счёта 500 секунд.
# Тег, в названии локации, указывающий на время - 'tm'.
#
# 2) сражаться с монстрами:
#   -- сражение имитируется списанием со счета персонажа N-количества времени и получением N-количества опыта
#   -- опыт и время указаны в названиях монстров (после exp указано значение опыта и после tm указано время)
# Так, если в локации вы обнаружили монстра Mob_exp10_tm20 (или Boss_exp10_tm20)
# необходимо списать со счета 20 секунд и добавить 10 очков опыта.
# Теги указывающие на опыт и время - 'exp' и 'tm'.
# После того, как игра будет готова, сыграйте в неё и наберите 280 очков при положительном остатке времени.

# По мере продвижения вам так же необходимо вести журнал,
# в котором должна содержаться следующая информация:
# -- текущее положение
# -- текущее количество опыта
# -- текущая дата (отсчёт вести с первой локации с помощью datetime)
# После прохождения лабиринта, набора 280 очков опыта и проверки на остаток времени (remaining_time > 0),
# журнал необходимо записать в csv файл (назвать dungeon.csv, названия столбцов взять из field_names).

# Пример лога игры:
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 1234567890.0987654321 секунд
# Прошло уже 0:00:00
# Внутри вы видите:
# -- Монстра Mob_exp10_tm0
# -- Вход в локацию: Location_1_tm10400000
# -- Вход в локацию: Location_2_tm333000000
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Выход
import csv
import json
import time
from decimal import *
import re

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


# Учитывая время и опыт, не забывайте о точности вычислений!

class DungeonAndDragons:
    """
    Мини игра на закрепление теории. Используется json файл: rpg.json
        Из теории: Регулярные выражения, .csv файлы, decimal и  date and time
    """

    def __init__(self, remaining_time, filename):
        self.number_of_action = None
        self.list_ = None
        self.remaining_time = Decimal(remaining_time)
        self.location = None
        self.file = filename
        self.list = None  ########### кол-во элементов и лист словарей
        self.number_of_jsonlist = None
        self.list_of_location_and_monsters = []
        self.dict_of_location = {}
        self.counter = None
        self.pattern_exp = r'p\d*'
        self.pattern_time = r'tm\d*.\d*'
        self.pattern_location = r'Location_\w\w*'
        self.exp = 0
        ### "Можно было бы куда-нибудь вынести"
        self.list_from_fieldnames = [field_names, ]
        self.list_with_values = []

    def game_progress(self):
        """
        Основной метод программы - запуск игры.
        Чтобы победить надо обязательно дойти до любой конечной локации (Ситуация, когда нет выбора новой локации).
        Набрать 280 опыта.
        И чтобы время (self.remaining_time) было больше нуля.  
        :return: None
        """
        self.file_open()
        print(f'У вас осталось  {self.remaining_time} секунд')
        print(f'У вас {self.exp} опыта')
        while True:
            self.enter_the_dungeon()
            self.action()
            if self.counter == 0:
                print('Конец игры')
                break
        if self.exp >= 280 and self.remaining_time > 0:
            print('Ура, победа')
            self.save_file()
        else:
            print('Судьба выбросила d1 и Ужастик настиг вас - вы проиграли, м...пук')

    def file_open(self):
        """
        Открытие файла rpg.json и заполнение списка (self.list) файлом .json
        :return: None
        """
        with open(file=self.file, mode="r", encoding="utf8") as json_file:
            json_list = json.load(json_file)
            self.list = []
            self.list.append(json_list)
            self.number_of_jsonlist = len(self.list)

    def save_file(self):
        """
        Сохранение данных в файл.csv при успешном прохождении игры. С данными о текущей локации, опыте и остатке времени
        :return: None 
        """
        loc = str(re.findall(self.pattern_location, self.location))[
              1:-1]  # Преобразование названия локации для красивого вывода
        self.list_with_values = [loc, self.exp, self.remaining_time]

        with open('dungeon.csv', 'w', newline='') as out_file:
            writer = csv.DictWriter(out_file, delimiter=',', fieldnames=self.list_from_fieldnames[0])
            line_of_parameters = {x: y for x, y in zip(field_names, field_names)}
            writer.writerow(line_of_parameters)
            first_line_names = {x: y for x, y in zip(field_names, self.list_with_values)}
            writer.writerow(first_line_names)

    def enter_the_dungeon(self):
        """
        Вывод всей информации о монстрах и локациях на консоль.
        #В теории можно было реализовать здесь переход в метод self.action(), а не в цикле метода def game_progress()
        :return: None
        """
        for number in range(self.number_of_jsonlist):
            self.list_ = self.list[number]
            if isinstance(self.list_, dict):
                for key, values in self.list_.items():
                    print(f'Вы находитесь в {key}')
                    counter_values = len(values)
                    print('Внутри вы видите:')
                    count = 1 # Счетчик для вывода действий
                    if len(self.list_of_location_and_monsters) == 0:
                        for k in range(counter_values):
                            if isinstance(self.list_[key][k], list):
                                for element in self.list_[key][k]:
                                    self.list_of_location_and_monsters.append(element)
                                    print(f'{count}. Убить -- Монстра: {element}')
                                    count += 1
                            elif 'exp' in self.list_[key][k]:
                                self.list_of_location_and_monsters.append(self.list_[key][k])
                                print(f'{count}. Убить -- Монстра: {self.list_[key][k]}')
                                count += 1
                            else:
                                for location, _ in self.list_[key][k].items():
                                    self.list_of_location_and_monsters.append(location)
                                    self.dict_of_location[location] = self.list_[key][k]
                                    print(f'{count}. Перейти -- Вход в локацию: {location}')
                                    count += 1
                                    self.location = location
                    else:
                        counter_loc = 0
                        counter_mons = len(self.list_of_location_and_monsters) * 2
                        for loc_or_mons in self.list_of_location_and_monsters:

                            if 'exp' in loc_or_mons:
                                print(f'{count}. Убить -- Монстра: {loc_or_mons}')
                                counter_mons -= 1
                                count += 1
                            elif 'Loc' in loc_or_mons:
                                print(f'{count}. Перейти -- Вход в локацию: {loc_or_mons}')
                                counter_loc += 1
                                count += 1
                        if counter_loc == 0 and counter_mons == 1:
                            '''Это для проверки, если будет список состоящих только из монстров(тупик с монстрами)'''
                            self.counter = 0

    def action(self):
        """
        Действия игрока:
        Перейти в локацию или убить монстра.
        :return: None
        """
        # print(self.list_of_location_and_monsters) #!
        while True:
            self.number_of_action = int(input('Чтобы выйти из игры нажмите 0\nВведите номер действия: '))
            print('_______' * 9)
            if self.number_of_action > len(self.list_of_location_and_monsters) or self.number_of_action < 0:
                print('Вышли за диапазон номера действий')
                continue
            elif self.number_of_action == 0:
                self.counter = 0
                """Выход из игры при вводе 0"""
                return False
            else:
                break

        index = self.number_of_action - 1
        value_from_index = self.list_of_location_and_monsters[index]

        if 'exp' in self.list_of_location_and_monsters[index]:
            self.changing_statistics(value_from_index)
            del self.list_of_location_and_monsters[index]
        elif 'Loc' in self.list_of_location_and_monsters[index]:
            key = self.list_of_location_and_monsters[index]
            self.list.clear()
            value = self.dict_of_location[key]
            self.list.append(value)  #
            self.number_of_jsonlist = len(self.list)
            self.changing_statistics(value_from_index) #УЧИТЫВАЕМ ВРЕМЯ И ЭКСПУ ПРИ ПЕРЕХОДЕ В КАЖДУЮ ЛОКАЦИЮ или ПРИ У монстра
            self.list_of_location_and_monsters.clear()

    def changing_statistics(self, value_from_index):
        """
        Получаем при помощи регулярок значение и меняем данные об текущем опыте и остатке времени
        :param value_from_index: элемент списка (это строка с названием локации или монстра)
        :return:
        """
        # mob_pattern = r'[M]em\w{,2}' #"Mob_exp20_tm167710"
        # loc_pattern = r'[Nn]em\w{,2}' #"Location_2_tm333000000":
        time_ = float(str(re.findall(self.pattern_time, value_from_index))[4:-2])

        # loc = re.findall(self.pattern_location, self.location)
        # print(loc)
        if 'exp' in value_from_index:
            exp_ = float(str(re.findall(self.pattern_exp, value_from_index))[3:-2])  # &&&&&???????
            self.exp += exp_


        self.remaining_time = Decimal(self.remaining_time) - Decimal(time_)
        print(f'Осталось {self.remaining_time} секунд')
        print(f'У вас {self.exp} опыта')


if __name__ == "__main__":
    dnd = DungeonAndDragons(remaining_time=remaining_time, filename='rpg.json')
    dnd.game_progress()
