# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
total_expenses = expenses
total_grant = educational_grant
i = 1
while i < 10:
    expenses += expenses * 3 / 100
    total_expenses += expenses
    total_grant += educational_grant

    i += 1
print(i)
result = round((total_grant - total_expenses) * (-1), 2)
print(f'Студенту надо попросить {result} рублей')
#37566.551737648784
