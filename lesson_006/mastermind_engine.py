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
    print(_pick_n)
    if _pick_n[0] == 0:
        _pick_n[0] = random.sample(seq_to_check, 1)
        number_1_with_index_0 = _pick_n[0][0]
        _pick_n[0] = number_1_with_index_0


def check_number(number):
    """Проверим число"""
    # for position in range(0,4):
    #     for number_ in pick_n: # number_ продумать имя
    #         if number_[0] != 0:
    #             if number_[position] ==
    # if
    # pass
pick_a_number()
print(_pick_n)