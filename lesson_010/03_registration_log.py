# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.
def check_file(line):
    name, email, age = line.split(' ')
    age = int(age)
    if name.isdigit():
        raise BaseException('NotNameError')
    elif not ('@' or '.') in email:
        raise BaseException('NotEmailError')
    elif not 10 <= age <= 99:
        raise ValueError
    else:
        # with open('registrations_good.log', mode='w', encoding='utf8') as log_good:
        #     log_good.write(f'{line}\n')
        log_good = open('registrations_good.log', 'a', encoding='utf8')
        log_good.write(f'{line}\n')
        log_good.close()
########### Чекнуть инфу по поводу записи в файлы
    # elif:
    #     raise ValueError
    ##return line
with open('registrations.txt', mode='r', encoding='utf8') as file_registrations:
    for line in file_registrations:
        line = line[:-1]
        try:
            check_file(line)
            ###ЗАПИСЬ
        except ValueError as exc:
            # if 'unpack' in exc.args[0]:
            #     print(f'Не хватает операндов {exc.args}')
            # else:
            print(f'Не могу преобразовать к целому числу {exc} в строке {line}')
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')


