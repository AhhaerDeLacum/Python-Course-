# -*- coding: utf-8 -*-
import os
import cv2
from datetime import datetime
# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды

# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому


class ImageMaker:
    """Создание новой директории для сохранения визиток-карточек"""
    project = os.path.abspath(os.curdir)
    image_cards_directory = "image_cards"
    PATH_IMAGE_CARDS_DIRECTORY = os.path.join(project, image_cards_directory)
    os.makedirs(PATH_IMAGE_CARDS_DIRECTORY, exist_ok=True)

    def __init__(self, weather_from_data=None, path_cards_directory=PATH_IMAGE_CARDS_DIRECTORY):
        self.example_of_postcard = 'weather_img/probe.jpg'
        self.image = None
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.weather_cloud = 'weather_img/cloud.jpg'
        self.weather_rain = 'weather_img/rain.jpg'
        self.weather_snow = 'weather_img/snow.jpg'
        self.weather_sun = 'weather_img/snow.jpg'
        self.image_weather = None
        self.path_cards_directory = path_cards_directory
        self.weather = weather_from_data
        self.run()
        self.type_of_color = None

    def save(self, image, day):
        path = os.path.join(self.image_cards_directory, f'{self.weather.month}')
        path = os.path.normpath(path)
        # 'lesson_016/python-virtual-environments/env/image_cards/ноя'
        #C:\Users\mrfen\PycharmProjects\probe\lesson_016\python-virtual-environments\env\image_cards\ноя
        month = self.weather.month
        # month = self.weather.month.encode(encodings='cp1251')
        #lesson_016/python-virtual-environments/env/image_cards/ноя
        # month = self.weather.month(encodings='cp1251')
        os.makedirs(path, exist_ok=True)
        # cv2.imwrite(f'{day}_{month}.jpg', image)
        # cv2.imwrite(f'{day}_{month}', image)
        # cv2.imwrite(f'{day}_'+month+'_.jpg', image)
        # cv2.imwrite(u'{}_{}.jpg'.format(day, month), image)
        now = datetime.now()
        month = now.month
        cv2.imwrite(f'{path}/{day}_{month}.jpg', image)
        # os.path.abspath()

    def select_properties_for_methods(self):
        # self.image_weather = cv2.imread(self.weather_sun)
        if 'дожд' in self.weather.weather.lower():
            self.image_weather = cv2.imread(self.weather_rain)
            self.type_of_color = 2
        elif 'солн' in self.weather.weather.lower():
            self.image_weather = cv2.imread(self.weather_sun)
            self.type_of_color = 1
        elif 'снеж' in self.weather.weather.lower():
            self.image_weather = cv2.imread(self.weather_snow)
            self.type_of_color = 4
        else:
            self.image_weather = cv2.imread(self.weather_cloud)
            self.type_of_color = 3
            # self.image_weather = cv2.imread(self.weather_sun)
        """Если погода такая-то, на основе этих условий надо вставлять в image_weather путь до картинки + еще тип для
        метода """

    def run(self):
        # self.open_probe_image()
        self.select_properties_for_methods()
        self.paint_postcard()
        self.put_text_on_postcard()
        self.add_image_on_postcard()
        self.save(self.image, self.weather.day_id)

    def add_image_on_postcard(self):
        img_background = self.image
        img_weather = self.image_weather

        brows, bcols = img_background.shape[:2]
        rows, cols, channels = img_weather.shape
        # Ниже я изменил roi, чтобы картинка выводилась посередине, а не в левом верхнем углу
        roi = img_background[0:rows, 0:cols]

        img2gray = cv2.cvtColor(img_weather, cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)

        img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

        img2_fg = cv2.bitwise_and(img_weather, img_weather, mask=mask)

        dst = cv2.add(img1_bg, img2_fg)
        img_background[int(brows / 2) - int(rows / 2):int(brows / 2) + int(rows / 2), int(bcols / 2) -
                                                                            int(cols / 2):int(bcols / 2) + int(
            cols / 2)] = dst
        self.image = img_background
        # cv2.imwrite('res.jpg', img_background)


    def put_text_on_postcard(self):
        cv2.putText(self.image, 'Day_of_week', (70, 80), self.font, 0.5, (0, 0, 0), 1, cv2.LINE_AA)
        # cv2.putText(self.image, f'{self.weather.day_of_week}', (70, 80), self.font, 0.5,
        #             self.color_text_date, 1, cv2.LINE_AA)
        # cv2.putText(self.image, f'{self.weather.day_id}', (70, 110), self.font, 0.4,
        #             self.color_text_date, 1, cv2.LINE_AA)
        # cv2.putText(self.image, f'{self.weather.month}', (70, 140), self.font, 0.4,
        #             self.color_text_date, 1, cv2.LINE_AA)
        # cv2.putText(self.image, f'{self.weather.weather}', (20, 20), self.font, 0.4,
        #             self.color_text_weather, 1, cv2.LINE_AA)
        # cv2.putText(self.image, f'Минимальная температура: {self.weather.min_temperature}', (200, 200), self.font, 0.35,
        #             self.color_text_weather, 1, cv2.LINE_AA)
        # cv2.putText(self.image, f'Максимальная температура: {self.weather.max_temperature}', (200, 220), self.font,
        #             0.35,
        #             self.color_text_weather, 1, cv2.LINE_AA)

    def open_probe_image(self):
        def viewImage(image, name_of_window):
            cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
            cv2.imshow(name_of_window, image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def paint_postcard(self):
        image_cv2 = cv2.imread(self.example_of_postcard)
        if self.type_of_color == 1:
            # image_with_sunny = image_cv2.copy()
            i = 0
            k = 0
            for _ in range(150):
                image_cv2[:, 0 + i:50 + i] = (50 + k, 255 - k / 8, 238)
                # image_with_sunny[:, 0 + i:50 + i] = (50 + k, 255 - k / 8, 238)
                i += 20
                k += 5
            # self.image = image_cv2
            # self.viewImage(image_cv2, 'Sunny')
        elif self.type_of_color == 2:
            i = 0
            k = 0
            for _ in range(150):
                image_cv2[:, 0 + i:50 + i] = (245, 110 + k/4, 95 + k/2)
                i += 20
                k += 5
        elif self.type_of_color == 3:
            i = 0
            k = 0
            for _ in range(150):
                image_cv2[:, 0 + i:50 + i] = (117 + k/4, 25 + k / 8, 0 + k / 4)
                i += 5
                k += 5
        elif self.type_of_color == 4:
            i = 0
            k = 0
            for _ in range(150):
                image_cv2[:, 0 + i:50 + i] = (56 + k/4, 56 + k/4, 56 + k/4)
                i += 5
                k += 4
        self.image = image_cv2


    def viewImage(self, image, name_of_window):
        cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
        cv2.imshow(name_of_window, image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        self.image = image


if __name__ == "__main__":
    imagemaker = ImageMaker()
    imagemaker.run()
# image_maker = ImageMaker()
# image_maker.run()