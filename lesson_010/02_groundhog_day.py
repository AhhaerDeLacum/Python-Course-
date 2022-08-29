# -*- coding: utf-8 -*-
import random
# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
ENLIGHTENMENT_CARMA_LEVEL = 777
CARMA_LEVEL = 0
def one_day():
    dice_random = random.randint(1, 13)
    #dice_random_exc = random.randint(1, 6)
    dice_random_carma = random.randint(1, 7)
    if dice_random == 1:
        try:
            raise BaseException('IamGodError')
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')
    if dice_random == 2:
        try:
            raise BaseException('DrunkError')
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')
    if dice_random == 3:
        try:
            raise BaseException('CarCrashError')
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')
    if dice_random == 4:
        try:
            raise BaseException('GluttonyError')
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')
    if dice_random == 5:
        try:
            raise BaseException('DepressionError')
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')
    if dice_random == 6:
        try:
            raise BaseException('SuicideError')
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')
    return dice_random_carma


while True:
    if CARMA_LEVEL < ENLIGHTENMENT_CARMA_LEVEL:
        print(CARMA_LEVEL)
        CARMA_LEVEL += one_day()
    else:
        break

# https://goo.gl/JnsDqu
