#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопаркее

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль
zoo.insert(1, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль
zoo.extend(birds)
print(zoo)
# уберите слона
#  и выведите список на консоль
zoo.remove('elephant')
# del zoo[3]
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.
index_lion = zoo.index('lion') + 1
index_lark = zoo.index('lark') + 1
print(f'Лев сидит в {index_lion} клетке, а жаворонок в {index_lark}')

