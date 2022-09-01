# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


# def get_prime_numbers(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#     return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик
"""class PrimeNumbers:
    def __init__(self, n):
        self.n, self.i, self.numbers = n, 1, []

    def __iter__(self):
        self.i = 1
        return self

    def get_prime_numbers(self):
        self.i += 1
        for prime in self.numbers:
            if self.i % prime == 0:
                return False
        return True

    def __next__(self):
        while self.i < self.n:
            if self.get_prime_numbers():
                self.numbers.append(self.i)
                return self.i
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10)
for number in prime_number_iterator:
    print(number)"""
# class PrimeNumbers:
#     def __init__(self, n):
#         self.n, self.i, self.number, self.counter = n, 1, [], 0
#
#     def __iter__(self):
#         self.i = 1
#         return self
#
#     # def __next__(self):
#     #     self.i += 1
#     #     if self.i > 0:
#     #         if self.i > self.n:
#     #             raise StopIteration()
#     #         for prime in self.number:
#     #             if self.i % prime == 0:
#     #                 break
#     #         else:
#     #             self.number.append(self.i)
#     #             self.counter += 1
#     #             if self.i is not None:
#     #                 return self.i
#     def get_prime_numbers(self):
#         self.i += 1
#         for prime in self.number:
#             if self.i % prime == 0:
#                 return False
#         return True
#
#     def __next__(self):
#         while self.i < self.n:
#             if self.get_prime_numbers():
#                 self.number.append(self.i)
#                 return self.i
#         else:
#             raise StopIteration()
#
#
# prime_number_iterator = PrimeNumbers(n=10)
# for number in prime_number_iterator:
#     print(number)


# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик
""" Интересный способ создания генератора натуральных чисел, нашел альтернативные решения
def is_prime(num):
    if num == 2: return True
    if num % 2 == 0: return False
    for _ in range(3, num // 2, 2):
        if num % _ == 0:
            return False
    return True

def primes():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1

print(list(itertools.takewhile(lambda x : x <= 10000, primes())))
"""

# def prime_numbers_generator(n):
#     prime_numbers = []
#     for number in range(2, n+1):
#         for prime in prime_numbers:
#             if number % prime == 0:
#                 break
#         else:
#             prime_numbers.append(number)
#             yield number
#
#
# for number in prime_numbers_generator(n=10000):
#     print(number)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
def numbers_generator(lucky_number):
    len_ = len(str(lucky_number))
    str_lucky_number = str(lucky_number)#132 2345
    if len_ >= 3:
        if len_ % 2 == 0:#4 6 8
            if int(str_lucky_number[0]) + int(str_lucky_number[1]) == int(str_lucky_number[-1]) + int(str_lucky_number[-2]):
                return True
            else:
                return False
        elif len_ % 2 == 1: #1 -1
            if int(str_lucky_number[0]) == int(str_lucky_number[-1]):
                return True
            else:
                return False
    else:
        return False

def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number # ЕСЛИ ЗАКОМЕНИТЬ ДВЕ НИЖНИЕ СТРОКИ И РАССКОМЕНТИТЬ ЭТУ, ТО ПОЛУЧАТСЯ ВСЕ НАТУРАЛЬНЫЕ ЧИСЛА
            # А так выводит только числа под фильтр
            # if numbers_generator(number):
            #     yield number


for number in prime_numbers_generator(n=10000):
    print(number, numbers_generator(number))

# for number in numbers_generator(n=100, lucky_number=727):
#     print(number)