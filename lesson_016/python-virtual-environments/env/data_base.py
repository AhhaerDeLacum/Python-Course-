# -*- coding: utf-8 -*-
import peewee
database = peewee.SqliteDatabase("db/weather.db")


class BaseTable(peewee.Model):
    # В подклассе Meta указываем подключение к той или иной базе данных
    class Meta:
        database = database


class Day(BaseTable):
    name = peewee.CharField(unique=True)


class Weather(BaseTable):
    day = peewee.ForeignKeyField(Day)
    month = peewee.CharField()
    day_of_week = peewee.CharField()
    weather = peewee.DateTimeField()
    max_temperature = peewee.CharField()
    min_temperature = peewee.CharField()


database.create_tables([Day, Weather])


class DatabaseUpdater:
    def __init__(self, d_m_dict, date_from=0, date_by=0):
        self.db = database
        self.days_dict = d_m_dict
        self.date_from = date_from
        self.date_by = date_by

    def write_data_into_db(self):
        for day, data in self.days_dict.items():
            try:
                Day(name=day).save()
                Weather.insert_many(data).execute()
            # except BaseException as exc: ########?
            except peewee.IntegrityError:
                pass

    def get_data_from_database(self):
        return Weather.select().where(Weather.day_id.between(self.date_from, self.date_by))


if __name__ == "__main__":
    DatabaseUpdater()