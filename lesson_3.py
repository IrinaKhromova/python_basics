# Ирина Хромова ДЗ 3

print('Задание 1')  # задание 1


def division(num, div):
    return num / div


try:
    num = int(input('Делимое: '))
    div = int(input('Делитель: '))
    division(num, div)
except ZeroDivisionError:
    print(f'Недопустимая операция: деление на ноль')
else:
    print(f'Результат деления: {division(num, div)}')


print('Задание 2')  # задание 2


def user(name, surname, birth_year, city, email, phone):
    data = {
        'Имя': name,
        'Фамилия': surname,
        'Год рождения': birth_year,
        'Город проживания': city,
        'E-mail': email,
        'Телефон': phone
    }
    return data


name = input('Имя: ')
surname = input('Фамилия: ')
birth_year = input('Год Рождения: ')
city = input('Город проживания: ')
email = input('E-mail: ')
phone = input('Телефон: ')

print(user(name, surname, birth_year, city, email, phone))


print('Задание 3')  # задание 3


def my_list():
    i = 1
    while len(li) < 3:
        el = float(input(f'Введите {i}-е число: '))
        li.append(el)
        i += 1
    return li


def my_func():
    my_list()
    for el in li:
        if el is min(li):
            li.remove(el)
            result3 = sum(li)
            return result3


li = []
print(f'Исходный список: {my_list()}')
print(f'Сумма двух максимальных элементов = {my_func()}')


print('Задание 4')  # задание 4


def input_xy():
    global x, y
    x = float(input('Введите действительное положительное число, основание степени X: '))
    if x < 0:
        x = float(input('Нужно ввести положительное число: '))
    try:
        y = int(input('Введите целое отрицательное число, показатель степени Y: '))
    except ValueError:
        y = int(input('Нужно ввести целое число: '))
    if y >= 0:
        y = int(input('Нужно ввести отрицательное число: '))
    return x, y


def my_func4_1(a, b):
    result4_1 = a ** b
    return result4_1


def my_func4_2(a, b):
    step = 1
    result4_2 = 1 / a
    while step < abs(b):
        result4_2 = result4_2 / a
        step += 1
    return result4_2


x = None
y = None
try:
    input_xy()
    my_func4_1(x, y)
    my_func4_2(x, y)
except ZeroDivisionError:
    print(f'Недопустимая операция: деление на ноль, x должно быть > 0')
    input_xy()

print(f'Результат по методу "X**Y": {my_func4_1(x, y)}')
print(f'Результат при помощи цикла 1/(X**|Y|): {my_func4_2(x, y)}')


print('Задание 5')  # задание 5


def calculate_sum(numbs):
    stop = False
    sum_numbers = 0
    for numb in numbs:
        try:
            if numb:
                sum_numbers += float(numb)
        except ValueError:
            stop = True
    return sum_numbers, stop


total_sum = 0

while True:
    user_numbers = input('Введите числа через пробел, чтобы закончить: буква или символ сразу или после чисел: ').split(' ')
    user_sum, finish = calculate_sum(user_numbers)
    total_sum += user_sum
    print(f'Сумма: {total_sum}')

    if finish:
        break


print('Задание 6 и 7')  # задание 6 и 7


def int_func(text):
    return text.title()


def title_word():
    title_ = []
    for word_title in input('Введите слова через пробел прописными буквами: ').split(' '):
        title_.append(int_func(word_title))
    return ' '.join(title_)


def sentence():
    sentence_ = []
    for word_sent in input('Введите слова через пробел прописными буквами: ').split(' '):
        sentence_.append(word_sent)
        if word_sent == sentence_[0]:
            sentence_.pop(0)
            sentence_.insert(0, int_func(word_sent))
    return ' '.join(sentence_)


print(f'Каждое слово с заглавной буквы: {title_word()}')
print(f'Как предложение: {sentence()}')

        
