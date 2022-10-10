# -*- coding: utf-8


class WeatherMaker:

    def __init__(self):
        self.no_exit = True
        self.number_of_action = None
        self.dict_of_actions = {
            1: {"text_of_action": "Обновить базу данных", "method": self.add_to_bd()},
            2: {"text_of_action": "Извлечь данные из базы данных", "method": self.pull_from_bd()},
            3: {"text_of_action": "Печать на консоль сведения о погоде", "method": self.print_weather_on_console()},
            4: {"text_of_action": "Создание открытки с погодой", "method": self.add_to_bd()},
        }


    def add_to_bd(self):
        pass

    def pull_from_bd(self):
        pass

    def print_weather_on_console(self):
        pass

    def make_a_postcard(self):
        pass

    def run(self):
        while self.no_exit:
            print("Погода для Наро-Фоминска. Выберите номер действия. ")
            for number, action in self.dict_of_actions.items():
                print(number, action['text_of_action'])
            self.number_of_action = int(input(''))
            if self.number_of_action > 4 or self.number_of_action < 1:
                print('Ошибка! Введите корректный номер действия\n')
                continue
            self.dict_of_actions[self.number_of_action]['method']
            self.do_u_want_to_exit()

    def do_u_want_to_exit(self):
        exit_ = int(input('Если вы хотите продолжить, то нажмите 1, а если выйти, то нажмите 2 '))
        if exit_ == 2:
            self.no_exit = False



weather_maker = WeatherMaker()
weather_maker.run()