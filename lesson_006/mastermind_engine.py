# В этом модуле нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов/
import random
_pick_n = []
SEQ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# POSITION = 0
def pick_a_number():
    """Загадываем число"""
    seq_to_check = []
    global _pick_n
    _pick_n = random.sample(SEQ, 4)
    seq_to_check = list(set(SEQ) - set(seq_to_check))  # 0123
    if _pick_n[0] == 0:
        _pick_n[0] = random.sample(seq_to_check, 1)
        number_1_with_index_0 = _pick_n[0][0]
        _pick_n[0] = number_1_with_index_0
    return _pick_n


def check_number(number):
    """Проверим число"""
    bulls = 0
    cows = 0
    for i in range(0, 4):
        number[i] = int(number[i])
    global _pick_n
    for i in range(0, len(number)):
        #print(number[i], '///')
        if number[i] == _pick_n[i]:
            bulls += 1
        for x in range(0, len(_pick_n)):
            #print(_pick_n[x])
            if (_pick_n[i] == number[x]) and (number[i] != _pick_n[i]):
                cows += 1
    dictionary = {'bulls': bulls, 'cows': cows}
    return dictionary
