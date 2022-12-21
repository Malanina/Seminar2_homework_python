# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые –
#  гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все
#  монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

import random
n = int(input('Введите количество монеток: '))
l = []
for i in range(n):
    random_number = round(random.randint(0, 1))
    l.append(random_number)
print(l)

conunt_reshka = l.count(int('0'))   # количество монеток, которые лежат вверх решкой
# print(conunt_reshka)
count_herb = n - conunt_reshka  # количество монеток, которые лежат вверх гербом
if conunt_reshka < count_herb:
    print(f'Нужно перевернуть {conunt_reshka}')
else:
    print(f'Нужно перевернуть {count_herb}')
if conunt_reshka == 0 or conunt_reshka == n:
    print(f'Переворачивать монетки не надо, все лежат одной стороной.')
