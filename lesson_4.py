# Ирина Хромова ДЗ 4

from sys import argv
from random import randint
from functools import reduce
from itertools import count, cycle
from math import factorial

print('Задание 1')  # задание 1

production, stake, bonus = map(float, argv[1:])
wages = production * stake + bonus
print('Выработка в часах: ', production)
print('Ставка в час: ', stake)
print('Премия: ', bonus)
print('Заработная плата: ', wages)

print('Задание 2')  # задание 2

n = 15
li_2 = [randint(0, 100) for i in range(n)]
print(li_2)
new_li = [li_2[i] for i in range(len(li_2)) if li_2[i] > li_2[i-1]]
print(new_li)

print('Задание 3')  # задание 3

print(f'Числа от 20 до 240, кратные 20 и 21: {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')

print('Задание 4')  # задание 4

m = 20
li_4 = [randint(10, 20) for i in range(m)]
print(li_4)
new = [num for num in li_4 if li_4.count(num) == 1]
print(new)

print('Задание 5')  # задание 5


def composition(prev_el, el):
    return prev_el * el


li_5 = [k for k in range(100, 1001) if k % 2 == 0]
print(li_5)
print(reduce(composition, li_5))

print('Задание 6')  # задание 6

print('Функция count')

a = 3
b = 10

for el_6 in count(a):
    if el_6 > b:
        break
    else:
        print(el_6)

print('Функция cycle')

li_6 = [randint(10, 30) for i in range(5)]
print(li_6)

с = 0
limit = 10

for el in cycle(li_6):
    if с >= limit:
        break
    print(el)
    с += 1

print('Задание 7')  # задание 7


def generator():
    for num in count(1):
        yield factorial(num)


fact = generator()

try:
    d = int(input('Введите целое положительное число для расчета факториала: '))
except ValueError:
    print('Нужно ввести целое число')
else:
    if d < 0:
        print('Число должно быть положительным')
    elif d == 0:
        print(1)
    else:
        i = 0
        for number in fact:
            if i >= d:
                break
            print(number)
            i += 1


