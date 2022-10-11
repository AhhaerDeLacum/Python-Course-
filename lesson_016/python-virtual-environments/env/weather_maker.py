# -*- coding: utf-8
from data_base import DatabaseUpdater
from weather import Weather
from image_maker import ImageMaker


class WeatherMaker:

    def __init__(self):
        self.data_not_none = None
        self.no_exit = True
        self.number_of_action = None
        self.dict_of_actions = {
            1: {"text_of_action": "Обновить базу данных", "method": self.add_to_bd},
            2: {"text_of_action": "Извлечь нужные данные из базы данных (Только потом действие 3)", "method": self.pull_from_bd},
            3: {"text_of_action": "Печать на консоль сведения о погоде", "method": self.print_weather_on_console},
            4: {"text_of_action": "Создание открытки с погодой", "method": self.make_a_postcard},
        }
        self.days_dict = {}

    def add_to_bd(self):
        self.days_dict = Weather().weather_per_days_dict
        DatabaseUpdater(self.days_dict).write_data_into_db()
        print('Данные на пару недель вперед загружены') #Можно будет сделать, чтобы загружалось только на 1-2 н вперед
        # print('000 -- ', self.days_dict)

    def pull_from_bd(self):
        print('Выберите интересующую дату. Например: От 1 до 31')
        day_from = input('C: ')
        day_by = input('И до: ')
        '''Для проверки, чтобы выводить на консоль или делать открытки'''
        self.data_not_none = DatabaseUpdater(self.days_dict, day_from, day_by).get_data_from_database()

    def print_weather_on_console(self):
        if self.data_not_none is None:
            self.pull_from_bd()
        for data in self.data_not_none:
            print(f'\nПогода на {data.day_id} {data.month} - {data.day_of_week}:\n----- {data.weather} -----\n'
                  f'Максимальная температура: {data.max_temperature}\n'
                  f'Минимальная температура: {data.min_temperature}')

    def make_a_postcard(self):
        if self.data_not_none is None:
            self.pull_from_bd()
        for data in self.data_not_none:
            ImageMaker(data)

    def run(self):
        while self.no_exit:
            print("Погода для Наро-Фоминска. Выберите номер действия. ")
            for number, action in self.dict_of_actions.items():
                print(number, action['text_of_action'])
            self.number_of_action = int(input(''))
            if self.number_of_action > 4 or self.number_of_action < 1:
                print('Ошибка! Введите корректный номер действия\n')
                continue
            self.dict_of_actions[self.number_of_action]['method']()
            self.do_u_want_to_exit()

    def do_u_want_to_exit(self):
        exit_ = int(input('Если вы хотите продолжить, то нажмите 1, а если выйти, то нажмите 2 '))
        """Проверка только на 2"""
        if exit_ == 2:
            self.no_exit = False


if __name__ == "__main__":
    # WeatherMaker()
    weather_maker = WeatherMaker()
    weather_maker.run()