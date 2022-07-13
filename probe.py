#1.Числа фибоначи*
from random import randint


def Fibonacci(f1):
    f2 = 1
    print(f1)
    while f2 < 1000:
        print(f2)
        f1, f2 = f2, f1 + f2

Fibonacci(1)

# f1, f2 = 1, 1
#     print(f1)
#     while f2 < 1000:
#         print(f2)
#         f1, f2 = f2, f1+f2

"""3.11"""
#Равнозначные "выражения"
zoo_pets = ['horse', 'lion', 'wolf', 'monkey', 'snake']
for i, animal in enumerate(zoo_pets):
    print(i, animal)


for i in range(len(zoo_pets)):
    animal = zoo_pets[0]
    print(i, animal)
#Распаковка словаря метод итемс для словаря, значения все под ключем и с ключем, а есть метод .values() он не возвращает
# ключ, только значения
zoo_pets_mass = {
    'horse': 400,
    'lion': 300,
    'wolf': 250,
    'monkey': 50,
    'snake': 7
}
total_mass = 0
for animal, mass in zoo_pets_mass.items():
    print(animal, mass)
    total_mass += mass
print('Общая масса животных', total_mass)

def some_func():
    print('xa xa')

result = some_func()
print(result)

"""3.17"""
from tkinter import *
mainwin = Tk ()
mainwin.mainloop()
''' 6.3'''
# def even_items(iterable):
#      """Возврат элементов ``iterable`` когда индекс четный"""
#      values = []
#      for index, value in enumerate(iterable, start=1):
#          if not index % 2:
#              values.append(value)
#      return values
# even_items()
_holder = []


def f1():
    global _holder
    _holder = []
    for i in range(5):
        _holder.append(randint(1, 20))
    print(_holder)
f1()
print(sum(_holder))
