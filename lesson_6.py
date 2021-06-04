# Ирина Хромова ДЗ 6

import time

print('Задание 1')  # задание 1


class Traffic_lights:
    __color = 'red'

    def running(self):
        print('Светофор работает')

        self.__color = 'red'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(7)

        self.__color = 'yellow'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(2)

        self.__color = 'green'
        print(f'Установлен цвет: {self.__color}')
        time.sleep(5)


t_1 = Traffic_lights()
print(t_1.running())

print('Задание 2')  # задание 2


class Road:

    def __init__(self, length, width):
        self._w = width
        self._l = length
        self.__asphalt_mass = 25
        self.__thickness = 0.05

    def calculate(self):
        return self._l * self._w * self.__asphalt_mass * self.__thickness


road = Road(5000, 20)
print(road.calculate())

print('Задание 3')  # задание 3


class Worker:

    def __init__(self, name, surname, wage, bonus):
        self.n = name
        self.s = surname
        self.wage = wage
        self.bonus = bonus
        self._inc = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def __init__(self, name, surname, wage, bonus):
        super(Position, self).__init__(name, surname, wage, bonus)

    def get_full_name(self):
        return f'{self.n} {self.s}'

    def get_total_income(self):
        total_income = sum([value for value in self._inc.values()])
        return f'Доход сотрудника {total_income} руб'


pos = Position('Vasily', 'Vasilev', 150000,  100000)
print(pos.get_full_name())
print(pos.get_total_income())

print('Задание 4')  # задание 4


class Car:

    def __init__(self, is_police, speed, color, name):
        self.p = is_police
        self.s = speed
        self.c = color
        self.n = name

    def go(self):
        return print('Поехали')

    def stop(self):
        return print('Приехали')

    def turn(self, direction):
        return print(f'Направляемся {direction}')

    def show_speed(self):
        return self.s


class PoliceCar(Car):
    def __init__(self, is_police, speed, color, name):
        super(PoliceCar, self).__init__(is_police, speed, color, name)


class TownCar(Car):
    def __init__(self, is_police, speed, color, name):
        super(TownCar, self).__init__(is_police, speed, color, name)

    def show_speed(self):
        if self.s > 60:
            return f'{self.n}. Скорость {self.s} км/ч. Превышение скорости!'
        else:
            return f'{self.n}. Скорость {self.s} км/ч'


class WorkCar(Car):
    def __init__(self, is_police, speed, color, name):
        super(WorkCar, self).__init__(is_police, speed, color, name)

    def show_speed(self):
        if self.s > 40:
            return f'{self.n}. Скорость {self.s} км/ч. Превышение скорости!'
        else:
            return f'{self.n}. Скорость {self.s} км/ч'


class SportCar(Car):
    def __init__(self, is_police, speed, color, name):
        super(SportCar, self).__init__(is_police, speed, color, name)


pc = PoliceCar(True, 100.0, 'White and blue', 'Lada Granta')
tc = TownCar(False, 80.0, 'Red', 'Kia K5')
wc = WorkCar(False, 40.0, 'Orange', 'Kamaz')
sc = SportCar(False, 180.0, 'Yellow', 'Ferrari')

pc.go()
print(wc.turn('налево'))
print(sc.turn('направо'))
print(wc.show_speed())
print(tc.show_speed())
print(f'Ferrari. Скорость {sc.show_speed()} км/ч')
pc.stop()

print('Задание 5')  # задание 5


class Stationery:
    title: str

    def draw(self):
        return 'Запуск отрисовки'


class Pen(Stationery):
    title = 'Pen'

    def draw(self):
        return f'Рисует ручка'


class Pencil(Stationery):
    title = 'Pencil'

    def draw(self):
        return f'Рисует карандаш'


class Handle(Stationery):
    title = 'Handle'

    def draw(self):
        return f'Рисует маркер'


p = Pen()
pc = Pencil()
h = Handle()
s = Stationery()

print(s.draw())
print(p.draw())
print(pc.draw())
print(h.draw())

