# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем
"""
BRUCE_WILLIS = 42

input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')

try:
    if len(input_data) < 5:
        raise IndexError('Выход за границы списка')
    leeloo = int(input_data[4])
except ValueError:
    print('невозможно преобразовать к числу')
    #if type(leeloo) != type(4):
    #if not isinstance(leeloo, int):
        #raise IndexError('Выход за границы списка')

result = BRUCE_WILLIS * leeloo
print(f"- Leeloo Dallas! Multi-pass № {result}!")
try:
    BRUCE_WILLIS = 42

    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except IndexError:
    print('indErr')
except ValueError:
    print('valueErr')
"""
try:
    BRUCE_WILLIS = 42

    input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f"- Leeloo Dallas! Multi-pass № {result}!")
except IndexError:
    print('выход за границы списка')
except ValueError:
    print('невозможно преобразовать к числу')
except:
    print('Упс, ошибочка неизвестная ')
# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
