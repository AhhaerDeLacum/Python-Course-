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
    if name is None or email is None or age is None:
        raise ValueError('ValueError')
    elif not name.isalpha():
        raise BaseException('NotNameError')
    elif not ('@' or '.') in email:
        raise BaseException('NotEmailError')
    elif not 10 <= age <= 99:
        raise ValueError('ValueError')

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
counter = 0
with open('registrations.txt', mode='r', encoding='utf8') as file_registrations:
    for line in file_registrations:
        counter += 1
        line = line[:-1]
        try:
            check_file(line)
            ###ЗАПИСЬ
        except ValueError as exc:
            if 'unpack' in exc.args[0]:
                print(f'Не хватает операндов {exc.args}')
                log_bad = open('registrations_bad.log', 'a', encoding='utf8')
                log_bad.write(f'{counter} {line} - {exc.args}\n') #(Не присутствуют все три поля)
                log_bad.close()
            else:
                print(f'Не входит в возрастные рамки {exc} в строке {line}')
                log_bad = open('registrations_bad.log', 'a', encoding='utf8')
                log_bad.write(f'{counter} {line} - {exc.args}\n')
                log_bad.close()
        except BaseException as exc:
            print(f'Исключение типа {exc.args}')
            log_bad = open('registrations_bad.log', 'a', encoding='utf8')
            log_bad.write(f'{counter} {line} - {exc.args}\n')
            log_bad.close()
        # except BaseException as exc:
        #     print(f'Исключение типа {exc.args}')
        #     log_bad = open('registrations_bad.log', 'a', encoding='utf8')
        #     log_bad.write(f'{line} - {exc.args}\n ')
        #     log_bad.close()

