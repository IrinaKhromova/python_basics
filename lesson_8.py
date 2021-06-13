# Ирина Хромова ДЗ 8

print('Задание 1')  # задание 1 (без учета реального количества дней в каждом месяце)


class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        date = []

        for i in day_month_year.split():
            if i != '-':
                date.append(i)

        return int(date[0]), int(date[1]), int(date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'Все верно'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Date.extract(self.day_month_year)}'


today = Date('28 - 5 - 2020')
print(today)
print(Date.valid(10, 11, 2022))
print(today.valid(4, 13, 2009))
print(Date.extract('15 - 8 - 2015'))
print(today.extract('7 - 11 - 2000'))
print(Date.valid(23, 10, 2008))

print('Задание 2')  # задание 2


class DivisionByZero(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    devidend = int(input('Введите делимое: '))
    division = int(input('Введите делитель: '))
    if not division:
        raise DivisionByZero('Деление на ноль')
    print(f'Результат {devidend/division}')

except ValueError:
    print('вы ввели не числа')
except DivisionByZero as error:
    print(error)

print('Задание 3')  # задание 3


class NotANumberException(Exception):
    def __init__(self, txt):
        self.txt = txt


res_list = []
while True:
    value = input('Введите элемент (число) для добавления в список или stop для выхода: ')

    if value.lower() == 'stop':
        print(f'Список на момент выхода{res_list}')
        break

    try:
        if not value.isnumeric():
            raise NotANumberException('NaN!')
        res_list.append(int(value))
    except NotANumberException as error:
        print('Вы ввели не число')

print('Задание 7')  # задание 7


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма чисел 1 и 2 равна')
        return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение чисел 1 и 2 равно')
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


i_1 = ComplexNumber(1, -3)
i_2 = ComplexNumber(3, 4)
print(i_1)
print(i_2)
print(i_1 + i_2)
print(i_1 * i_2)
