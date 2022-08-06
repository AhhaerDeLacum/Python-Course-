"""
Формат выходных данных

В единственной строке выведите максимальную прибыль, которую можно получить, поменяв данные за не более, чем два дня.



Замечание

Можно менять данные за не более, чем два дня, в том числе не менять ничего.
"""
earnings = 0
while True:
    n_days = int(input('Введите число дней '))
    if not 2 <= n_days <= 10 ** 5:
        print('Не входит в диапазон допустимых значений 1 входные данные')
        continue
    a_number_of_subs = input('Введите число подписок ').split()
    num_list = list(map(int, a_number_of_subs))
    for i, number in enumerate(num_list):
        if not 1 <= number <= 10 ** 3:
            print('Не входит в диапазон допустимых значений 2 входные данные')
            a_number_of_subs = input('Введите число подписок ').split()
            num_list = list(map(int, a_number_of_subs))
            continue
        earnings += ((-1) ** (i + 1 - 1)) * number

    break
print(abs(earnings))
