"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия. Для
выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""

from sys import argv

script_name, hour_total, hour_cost, bonus = argv

if hour_total.isnumeric() and hour_cost.isnumeric() and bonus.isnumeric():
    print('Зарплата сотрудника =', (float(hour_total) * float(hour_cost) + float(bonus)))
else:
    print('Неверно заданы параметры')