# Ирина Хромова ДЗ 2

# задание 1

li_1 = [1, 'd', 3.5, 'abc', 10]
print(li_1)

for i in range(0, len(li_1)):
    print('element', i, type(li_1[i]))

# задание 2

li_2 = []

while True:
    el = input('Введите элемент списка, чтобы закончить ввод введите end: ')
    if el.lower() == 'end':
        break
    li_2.append(el)
print(li_2)

print('Замена местами пар значений')

for i in range(1, len(li_2), 2):
    li_2[i], li_2[i-1] = li_2[i-1], li_2[i]
print(li_2)

# задание 3

print('через list')

month_el = (12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)

month_num = int(input('Введите номер месяца: '))

if month_num in month_el[:3]:
    print('is winter')
elif month_num in month_el[3:6]:
    print('is spring')
elif month_num in month_el[6:9]:
    print('is summer')
elif month_num in month_el[9:12]:
    print('is autumn')

if month_num <= 0 or month_num > 12:
    print('Такого месяца нет')

print('через dict')

season = {
    'is winter': [12, 1, 2],
    'is spring': [3, 4, 5],
    'is summer': [6, 7, 8],
    'is autumn': [9, 10, 11]
}
month = int(input('Введите номер месяца: '))

for key in season.keys():
    if month in season[key]:
        print(key)

if month <= 0 or month > 12:
    print('Такого месяца нет')

# задание 4

string = input('Введите несколько слов через пробелы: ')
string_1 = string.split()
len_max = 10

for i, v in enumerate(string_1, 1):
    if len(v) > len_max:
        v = v[:len_max]
    print(i, v)

# задание 5

my_list = [7, 5, 3, 3, 2]
print(my_list)

while True:
    try:
        elem = int(input('Введите целое число: '))
    except ValueError:
        print('Нужно ввести целое число!')
    else:
        my_list.append(elem)
        my_list.sort(reverse=True)
        print(my_list)
        stop_sort = input('Желаете продолжить? Если ДА, нажмите Enter (или любую клавишу), если НЕТ, введите N: ')
        if stop_sort.title() == 'N':
            break

# задание 6

products = []
description = {}
analytics = {}
num = 1

while True:
    start = input(f'Желаете заполнить описание товара {num} y/no: ')
    if start.lower() == 'no':
        break
    elif start.lower() == 'y':
        name = input('Введите название товара: ')
        cost = float(input('Введите цену: '))
        count = int(input('Введите количество: '))
        units = input('Введите единицы измерения: ')
        description = dict({'название': name, 'цена': cost, 'количество': count, 'ед': units})
        products.append(tuple([num, description]))
        num += 1

for product in products:    
    description = product[-1]
    for key, value in description.items():
        if key in analytics:
            if value not in analytics.get(key):
                analytics.get(key).append(value)
        else:
            analytics.update({key: [value]})

print(f'Список: {products}')
print(f'Аналитика: {analytics}')
