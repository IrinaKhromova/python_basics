# Ирина Хромова ДЗ 5

import json

print('Задание 1')  # задание 1

file = open('task1.txt', 'w',  encoding='utf-8')

while True:
    string = input('Введите что-либо, для выхода нажмите Enter в пустой строке: ')
    if not string:
        file.close()
        break
    file.write(f'{string}\n')

print('Задание 2')  # задание 2

with open('task2.txt', 'r', encoding='utf-8') as file2:
    lines = file2.readlines()
    print(f'В файле {len(lines)} строк(и)')
    i = 1
    for word in lines:
        print(f'В строке {i} {len(word.split())} слов')
        i += 1

print('Задание 3')  # задание 3

with open('task3.txt', 'r', encoding='utf-8') as file3:
    lines = file3.readlines()
    total = 0
    for row in lines:
        line = row.split()
        if float(line[1]) < 20000:
            print(f'{line[0]} Имеет оклад менее 20000 руб')
        total += float(line[1])
    average = total / len(lines)

print(f'Средняя величина дохода сотрудников: {average} руб')

print('Задание 4')  # задание 4

dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

with open('task4.txt', 'r', encoding='utf-8') as file_r:
    lines = file_r.readlines()

with open('task4-res.txt', 'w', encoding='utf-8') as file_w:
    for line in lines:
        row = line.split()
        row[0] = dictionary[row[0]]
        print(' '.join(row), file=file_w)

print('Задание 5')  # задание 5

nums = []
i = 1
while True:
    try:
        num = float(input(f'Введите {i} число, для завершения нажмите Enter без числа: '))
        nums.append(str(num))
    except ValueError:
        print('Ввод чисел завершен')
        break
    i += 1

with open('task5.txt', 'w', encoding='utf-8') as file_write:
    print(f'{" ".join(nums)}', file=file_write)

with open('task5.txt', 'r', encoding='utf-8') as file_read:
    nums_list = file_read.readline().split()
    nums_sum = 0
    for num in nums_list:
        nums_sum += float(num)

print(f'Сумма чисел:{nums_sum}')

'''
print('Задание 6')  # задание 6
# не смогла сделать, если 120(л). Попыталась, если в файле записано 120 (л), но тоже не получилось 
# жду разбор домашки, к сожалению нет времени докопаться до сути )

all_subject = {}
with open('task6.txt', 'r', encoding='utf-8') as file_read:
    lines = file_read.readlines()
    for line in lines:
        line.split(' ')
        hours = float(line[1]) + float(line[3]) + float(line[5])
        all_subject[line[0]] = hours

print(f'Всего часов по каждому предмету:\n {all_subject}')
'''


print('Задание 7')  # задание 7

result = []
profit = {}
average = []

with open('task7.txt', 'r', encoding='utf-8') as f_r:
    for line in f_r.readlines():
        row = line.split()
        profit[row[0]] = float(row[-2]) - float(row[-1])
        if profit[row[0]] > 0:
            average.append(profit[row[0]])

result = [profit, {'average_profit': round(sum(average) / len(average), 1)}]

with open('task7.json', 'w', encoding='utf-8') as f_w:
    json.dump(result, f_w)


