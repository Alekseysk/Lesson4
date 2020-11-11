"""
Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка
использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""


def generator(input_list):
    prev = input_list[0]
    for el in input_list:
        if el <= prev:
            prev = el
            continue
        prev = el
        yield el


orig_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

g = generator(orig_list)

processed_list = [elem for elem in g]

print(processed_list)