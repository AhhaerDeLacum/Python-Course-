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

import json

remaining_time = '1234567890.0987654321'
# если изначально не писать число в виде строки - теряется точность!
field_names = ['current_location', 'current_experience', 'current_date']


# Учитывая время и опыт, не забывайте о точности вычислений!

class DungeonAndDragons:

    def __init__(self, remaining_time, filename):
        self.remaining_time = remaining_time
        self.location = None
        self.file = filename
        self.list = None ########### кол-во элементов и лист словарей
        self.number_of_jsonlist = None

    def game_progress(self):
        self.file_open()
        #Условие вероятно надо
        i = 3
        while i != 0:
            i -= 1
            self.enter_the_dungeon()
            self.action()

    def file_open(self):
        with open(file=self.file, mode="r", encoding="utf8") as json_file:
            json_list = json.load(json_file)
            self.list = []
            self.list.append(json_list)
            self.number_of_jsonlist = len(self.list)

    def enter_the_dungeon(self):
        for number in range(self.number_of_jsonlist):
            print(self.list[number]) ##############
            self.list_ = self.list[number]
            # k = self.list[number].keys()
            # print(k)

            for key, values in self.list_.items():
                print(f'Вы находитесь в {key}')
                l = len(values)
                print('Внутри вы видите:')
                for k in range(l):
                    if 'exp' in self.list_[key][k]:
                        print('-- Монстра', self.list_[key][k])
                    else:
                        for location, _ in self.list_[key][k].items():
                            print(f'-- Вход в локацию: {location}' )
                    # print('Локация', fffa[key][k])
""" основная идея: нужно внутри метода enter_the_dungeon в конце сохранять значение локации и возможно монстров в
список новый self.(создать) и из него или же реализовать переход в методе game_progress в метод action() и потом 
менять вывод экрана, когда убит монстр и прочее ....
"""
            # print(self.list['Location_0_tm0'])
            # print(len(self.list['Location_0_tm0']))
            # print(self.list['Location_0_tm0'][0])
            # print(self.list['Location_0_tm0'][1])
            # print(self.list['Location_0_tm0'][2])
    def action(self):
        pass



dnd = DungeonAndDragons(remaining_time=remaining_time, filename='rpg.json')
dnd.game_progress()
