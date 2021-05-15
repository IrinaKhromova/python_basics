# Ирина Хромова ДЗ 1

# задание 1

print('Hello, world!')
print(5)
print(6.7)

n = 6
print(n)
print(str(n))

name = input('Введите имя: ')
age = int(input('Введите возраст: '))
age1 = age + 20
print(f' {name}, {age} лет. Через 20 лет Вам будет {age1} лет')

# задание 2

sec = int(input('Введите время в секундах: '))
hours = sec // 3600
sec = sec % 3600
minutes = sec // 60
sec = sec % 60

print(f'{hours:2}:{minutes:2}:{sec:2}')
# print('%02d:%02d:%02d' % (hours, minutes, sec))

# задание 3

n = input('Введите целое число n: ')
n2 = 2 * n
n3 = 3 * n
s = int(n) + int(n2) + int(n3)
print('сумма n + nn + nnn: ', s)

# задание 4

a = int(input('Введите целое положительное число: '))

b = a % 10
a = a // 10
while a > 0:
    if a % 10 > b:
        b = a % 10
    a = a // 10
print('Самая большая цифра числа: ', b)

# задание 5

revenue = int(input('Введите сумму прибыли, руб: '))
costs = int(input('Введите сумму издержек, руб: '))
profit = None
profitability = None
loss = None
staff = None
staff_profit = None

if revenue > costs:
    profit = revenue - costs
    profitability = profit / revenue
    print(f'Прибыль: {profit} руб; рентабельность: {profitability}')
    staff = int(input('Введите число сотрудников: '))
    staff_profit = profit / staff
    print(f'Прибыль в расчете на одного сотрудника: {staff_profit} руб')

else:
    loss = costs - revenue
    print(f'Убыток: {loss} руб')

# задание 6

print('БЕГУН')
a = 2
b = 3
day = 1
progress = 0.1

while True:
    print(f'{day} день: {a:5.2f} км')
    a = a + (a * progress)
    day += 1
    if a / b >= 1:
        break
sep = '\n'
print(f'{day} день: {a:5.2f} км {sep} на {day} день спортсмен достиг результата не менее {b} км')
