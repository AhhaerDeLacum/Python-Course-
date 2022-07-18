# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint


# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.


# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)
class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None
        self.cat = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_for_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.feed_food += 50
            self.house.money -= 50

    def clean_house(self):
        cprint('{} Убрался дома'.format(self.name), color='green')
        self.house.dirty -= 100
        self.fullness -= 20

    def pick_up_a_cat(self, house, cat):
        cprint('{} Взял кота'.format(self.name), color='green')
        self.house = house
        self.cat = cat
        self.cat.house = self.house

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    # Доработать класс человека, добавив методы
    #   подобрать кота - у кота появляется дом.
    #   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
    #   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
    # Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)
    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        # elif self.cat.fullness <= 0:
        #     cprint('{} умер кит...'.format(self.name), color='red')
        dice = randint(1, 6)


        #elif self.cat.fullness < 20: ###остановился ( надо доделывать методы для кота )
        if self.fullness < 21:
            self.eat()
        elif self.house.money < 100:
            self.work()
        if self.house.feed_food < 20:
            self.shopping_for_cat()

        elif self.house.food < 10:
            self.shopping()
        # elif self.house.feed_food < 20:
        #     self.shopping_for_cat()
        elif self.house.dirty >= 100:
            self.clean_house()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0
        self.feed_food = 0 # ne menishe 20
        self.dirty = 0

    def __str__(self):
        return 'В доме еды осталось {}, денег осталось {}, корма осталось {}, грязи {}'.format(
            self.food, self.money, self.feed_food, self.dirty)


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def sleep(self):
        cprint('{} поспал'.format(self.name), color='yellow')
        self.fullness -= 10

    def eaten(self):
        if self.house.feed_food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.feed_food -= 10
        else:
            cprint('{} нет корма'.format(self.name), color='red')

    def tear_up_the_wallpaper(self):
        cprint('{} дерет обои'.format(self.name), color='yellow')
        self.fullness -= 10
        self.house.dirty += 5

    def act_by_cat(self):
        if self.fullness <= 0:
            cprint('{} Умерчик...'.format(self.name), color='red')
            return
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eaten()
        if dice == 1:
            self.eaten()
        elif dice == 2:
            self.tear_up_the_wallpaper()
        else:
            self.sleep()


# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

citizens = [
    Man(name='Бивис'),
    # Man(name='Батхед'),
    # Man(name='Кенни'),
    #Cat()########################33
]


my_sweet_home = House()
kitty = Cat(name='Мистер малой')

for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)

Man(name='Бивис').pick_up_a_cat(house=my_sweet_home, cat=kitty)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    kitty.act_by_cat()
    print(kitty)
    print(my_sweet_home)
# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.


# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.



# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
