# -*- coding: utf-8 -*-

import os, time, shutil

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
class ScriptSortingByTime:
    def __init__(self):
        self.file_time = 0

    def open_dir(self):
        path = input('Введите путь вашей папки ')
        if path:
            path_normalized = os.path.normpath(path)
            for dirpath, dirnames, filenames in os.walk(path_normalized):
                print(dirpath, dirnames, filenames)

                for file in filenames:
                    full_file_path = os.path.join(dirpath, file)
                    secs = os.path.getmtime(full_file_path)
                    self.file_time = time.gmtime(secs)
                    print(self.file_time)
                    self._make_directory()
    def _make_directory(self):
        os.makedirs()
        if self

# secs = os.path.getmtime(full_file_path)
#         file_time = time.gmtime(secs)
#         if file_time[0] == 2013:
#             # выводим только файлы за 2013 год
#             print(full_file_path, secs, file_time)

script = ScriptSortingByTime()
script.open_dir()
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

# TODO здесь ваш код

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Основная функция должна брать параметром имя zip-файла и имя целевой папки.
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
