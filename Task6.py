"""
Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.

Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что
создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.

Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10
завершаем цикл. Во втором также необходимо предусмотреть условие, при котором повторение
элементов списка будет прекращено.
"""

from itertools import count, cycle


def iter_count(start, stop):
    result = count(start)
    for val in result:
        if val > stop:
            break
        yield val


def iter_cycle(cycle_list, stop):
    result = cycle(cycle_list)
    for ind, val in enumerate(result):
        if ind > stop:
            break
        yield val
       

i_count = iter_count(3, 10)
i_cycle = iter_cycle('qwer', 20)

print([val for val in i_count])
print([val for val in i_cycle])