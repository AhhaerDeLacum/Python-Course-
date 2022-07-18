# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())
class ElementResult:
    def __init__(self, element1, element2):
        self.element1 = element1
        self.element2 = element2
        self.elem_result = None  #########
        # if element2 != element1:
        #     self.elem_result = 'Щторм'
        if (str(element1) == 'Вода' and str(element2) == 'Воздух') or (
                str(element1) == 'Воздух' and str(element2) == 'Вода'):
            self.elem_result = 'Шторм'
        elif (str(element1) == 'Вода' and str(element2) == 'Огонь') or (
                str(element1) == 'Огонь' and str(element2) == 'Вода'):
            self.elem_result = 'Пар'
        elif (str(element1) == 'Вода' and str(element2) == 'Земля') or (
                str(element1) == 'Земля' and str(element2) == 'Вода'):
            self.elem_result = 'Грязь'
        elif (str(element1) == 'Огонь' and str(element2) == 'Воздух') or (
                str(element1) == 'Воздух' and str(element2) == 'Огонь'):
            self.elem_result = 'Молния'
        elif (str(element1) == 'Земля' and str(element2) == 'Воздух') or (
                str(element1) == 'Воздух' and str(element2) == 'Земля'):
            self.elem_result = 'Пыль'
        elif (str(element1) == 'Земля' and str(element2) == 'Огонь') or (
                str(element1) == 'Огонь' and str(element2) == 'Земля'):
            self.elem_result = 'Лава'

    def __str__(self):
        return str(self.elem_result)


class Water:
    def __init__(self):
        self.element = 'Вода'

    def __str__(self):
        return str(self.element)  #######################

    def __add__(self, other):
        return ElementResult(self, other)


class Air:
    def __init__(self):
        self.element = 'Воздух'

    def __str__(self):
        return str(self.element)  #######################

    def __add__(self, other):
        return ElementResult(self, other)


class Fire:
    def __init__(self):
        self.element = 'Огонь'

    def __str__(self):
        return str(self.element)  #######################

    def __add__(self, other):
        return ElementResult(self, other)


class Earth:
    def __init__(self):
        self.element = 'Земля'

    def __str__(self):
        return str(self.element)  #######################

    def __add__(self, other):
        return ElementResult(self, other)


print(Water(), '+', Air(), '=', Water() + Air())
print(Fire(), '+', Air(), '=', Fire() + Air())
# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
