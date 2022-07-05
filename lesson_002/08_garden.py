#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветыы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
print(garden_set)
print(meadow_set)

# выведите на консоль все виды цветов
all_flowers = garden_set | meadow_set
print(all_flowers) #

# выведите на консоль те, которые растут и там и там
all_flowers = garden_set & meadow_set
print(all_flowers)

# выведите на консоль те, которые растут в саду, но не растут на лугу
all_flowers = (garden_set | meadow_set) - meadow_set
print(all_flowers)

# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код


