# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Подвести итоги жизни за год: сколько было заработано денег, сколько съедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.dirt = 0

    def __str__(self):
        return 'Осталось денег - {}, еды - {}, степень грязи в доме - {}'.format(self.money, self.food, self.dirt)


# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
class Human:
    def __init__(self, name):
        self.name = name
        self.happiness = 100
        self.fullness = 30
        self.house = home

    def hungry(self):
        self.fullness -= 10

    def depression(self):
        if self.house.dirt >= 90:
            self.happiness -= 10

    def __str__(self):
        return '{} по имени {}. Уровень счастья - {}, уровень сытости - {}'.format(self.__class__.__name__, self.name,
                                                                                   self.happiness, self.fullness)


class Husband(Human):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()
        # '{} по имени {}'.format(self.__class__.__name__, self.name)
        # super().__str__()
        # '{} model {}'.format(self.__class__.__name__, self.model)

    # Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
    # Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 0:
            cprint('{} умерчик ...'.format(self.name), color='red')
            return
        elif self.happiness <= 10:
            cprint('{} умерчик от депрешн ...'.format(self.name), color='red')
            return
        if self.house.dirt > 90:
            self.happiness -= 10

        if self.fullness <= 10:
            self.eat()
        elif self.house.money <= 10:
            self.work()
        elif self.happiness <= 20:
            self.gaming()

        if dice == 1:
            self.eat()
        elif dice == 2:
            self.gaming()
        else:
            self.work()





    def eat(self):
        #self.rand_food = randint(1, 30)
        rand_food = randint(1, 20) #2 >20
        # if rand_food == 0:
        #     rand_food += 1
        if self.fullness > 40:
            cprint('{} Вместо еды решил поработать, потому что сытость - {}'.format(self.name, self.fullness),
                   color='magenta')
            self.work()
        elif self.fullness > 30:
            cprint('{} Вместо еды решил поиграть, потому что сытость - {}'.format(self.name, self.fullness),
                   color='magenta')
            self.gaming()
        elif self.house.food > rand_food:
            self.fullness += self.house.food
            self.house.food -= self.house.food
            cprint('{} поел теперь сытость равна - {}'.format(self.name, self.fullness), color='magenta')
        else:
            if self.house.food <= 0:
                cprint('Еда закончилась', color='red')

                #return
            else:
                self.house.food -= rand_food
                self.fullness += rand_food
                cprint('{} поел теперь сытость равна - {}'.format(self.name, self.fullness), color='magenta')
        #elif self.house.food <= 0:



    def work(self):
        if self.fullness > 10:
            self.hungry()
            self.house.money += 150
            global money_earned
            money_earned += 150
            cprint('Заработал 150 монет', color='magenta')
        else:
            cprint('{} слишком голоден, чтобы работать, сытость - {}'.format(self.name, self.fullness), color='red')
            self.eat()

    def gaming(self):
        if self.fullness > 10:
            self.hungry()
            self.happiness += 20
            cprint('Поиграл в WoT', color='magenta')
        else:
            cprint('{} слишком голоден, чтобы играть в WoT, сытость - {}'.format(self.name, self.fullness), color='red')
            self.eat()

#Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
class Wife(Human):

    def __init__(self, name):
        super().__init__(name=name)

    def __str__(self):
        return super().__str__()

    def act(self):
        dice = randint(1, 4)
        if self.fullness <= 0:
            cprint('{} сделала умерчик ...'.format(self.name), color='red')
            return
        elif self.happiness <= 10:
            cprint('{} совершила умерчик от депрешн ...'.format(self.name), color='red')
            return
        if self.house.dirt > 90:
            self.happiness -= 10

        if self.house.food < 60:
            self.shopping()
        elif self.fullness <= 30:
            self.eat()
        elif self.happiness <= 20:
            self.buy_fur_coat()
        elif self.house.dirt >= 100:
            self.clean_house()

        if dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.buy_fur_coat()
        else:
            self.clean_house()

    def eat(self):
        # self.rand_food = randint(1, 30)
        rand_food = randint(1, 20)  # 2 >20
        # if rand_food == 0:
        #     rand_food += 1
        if self.fullness > 40:
            cprint('{} Вместо еды решила купить еду {}, потому что сытость - {}'.format(self.house.food, self.name, self.fullness), color='magenta')
            self.shopping()
        elif self.fullness > 30:
            cprint('{} Вместо еды решила убраться дома, потому что сытость - {}'.format(self.name, self.fullness),
                   color='magenta')
            self.clean_house()
        elif self.house.food > rand_food:
            self.fullness += self.house.food
            self.house.food -= self.house.food

            cprint('{} поела теперь сытость равна - {}'.format(self.name, self.fullness), color='magenta')
        else:
            if self.house.food <= 0:
                cprint('Еда закончилась', color='red')

                # return
            else:
                self.house.food -= rand_food
                self.fullness += rand_food
                cprint('{} поела теперь сытость равна - {}'.format(self.name, self.fullness), color='magenta')
        # elif self.house.food <= 0:

    def shopping(self):
        if self.fullness >= 10:
            if self.house.money >= 20:
                self.house.money -= 20
                self.house.food += 20
                self.hungry()
                cprint('Купила еду за 20 монет. Еды - {}'.format(self.house.food), color='red')
            elif self.house.money >= 10:
                self.house.money -= 10
                self.house.food += 10
                self.hungry()
                cprint('Купила еду за 10 монет. Еды - {}'.format(self.house.food), color='red')
            else:
                cprint('Не хватает на еду. Дома только {}'.format(self.house.money), color='red')
            if self.fullness == 10:
                self.eat()
        else:
            cprint('{} слишком голодна, чтобы идти в магазин за едой {}'.format(self.name, self.fullness), color='red')
            self.eat()

    def buy_fur_coat(self):
        global all_fur_coat
        if self.fullness > 10:
            if self.house.money >= 350:
                self.house.money -= 350
                self.happiness += 60
                self.hungry()
                all_fur_coat += 1
                cprint('Купила шубу. Денег осталось - {}'.format(self.house.money), color='red')
            else:
                cprint('Не хватает на шубу. Дома только {}'.format(self.house.money), color='red')
        else:
            cprint('{} слишком голодна, чтобы идти в магазин за шубой {}'.format(self.name, self.fullness), color='red')
            self.eat()


    def clean_house(self):
        if self.fullness > 10:# 80 > 100
            if self.house.dirt >= 100:
                self.house.dirt -= 100
                self.hungry()
                cprint('{} убрала квартиру. Уровень чистоты {}'.format(self.name, self.house.dirt), color='red')
            else:
                self.house.dirt -= self.house.dirt
                self.hungry()
                cprint('{} убрала квартиру. Уровень чистоты {}'.format(self.name, self.house.dirt), color='red')
        else:
            cprint('{} слишком голодна, чтобы убираться {}'.format(self.name, self.fullness), color='red')
            self.eat()

money_earned = 0
all_fur_coat = 0
home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='yellow')
    serge.act()
    masha.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(home, color='cyan')
    home.dirt += 5
print('Кол-во заработанных монет за все время', money_earned)
print('Шубы', all_fur_coat)

# TODO после реализации первой части - отдать на проверку учителю

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


class Cat:

    def __init__(self):
        pass

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass

    def soil(self):
        pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

class Child:

    def __init__(self):
        pass

    def __str__(self):
        return super().__str__()

    def act(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        pass


# TODO после реализации второй части - отдать на проверку учителем две ветки


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murzik = Cat(name='Мурзик')

for day in range(365):
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    kolya.act()
    murzik.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(kolya, color='cyan')
    cprint(murzik, color='cyan')

# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
