import matplotlib.pyplot as plt
import numpy as np
from math import *

# Настройки

# количество сегментов в линиях
# чем больше чем точнее и тем медленнее
number_of_segments = 100

# цвета
fill_color = 'blue'
point_in_set_color = 'green'
point_not_in_set_color = 'red'

##########
# этап 1 #
##########
# считываем точку

px, py = map(float, input('Введите координаты точки: ').split())

# определяем в множестве ли точка?
is_poing_in_set = (((abs(px) <= 5 and abs(py) <= 1) |
                    (abs(py) <= 5 and abs(px) <= 1)) ^
                   (px ** 2 + py ** 2 <= 16))

# выбор цвета в зависимости он местонахождения
point_color = point_in_set_color if is_poing_in_set else point_not_in_set_color

# печать сообщения о местонахождении
if is_poing_in_set:
    print("Точка находится во множестве")
else:
    print("Точка во множестве нет")

##########
# этап 2 #
##########
# рисуем границы графиков или чёрные полоски

# для сохранения соотношения сторон графика
fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')


# функция, которая по заданному фи даёт координаты x,y
# для окружности с заданным адрессом
def cirlce_xy(r, phi):
    return r * np.cos(phi), r * np.sin(phi)


# диапазон углов от нуля до 2 пи с шагом 0.1
phis = np.arange(0, pi * 2, 0.01)
r = 4
ax.plot(*cirlce_xy(r, phis), c='k', ls='-')


# функция которая рисует линию
def line(point1, point2):
    ax.plot(np.linspace(point1[0], point2[0], number_of_segments),  # иксы
            np.linspace(point1[1], point2[1], number_of_segments),  # игрики
            color='k')  # чёрный цвет


# ресуем крест по координатам
line((-5, 1), (-1, 1))
line((5, 1), (1, 1))

line((-5, -1), (-1, -1))
line((5, -1), (1, -1))

line((1, -5), (1, -1))
line((1, 5), (1, 1))

line((-1, -5), (-1, -1))
line((-1, 5), (-1, 1))

line((-1, 5), (1, 5))
line((-1, -5), (1, -5))

line((5, -1), (5, 1))
line((-5, -1), (-5, 1))

##########
# этап 3 #
##########
# заливка областей принадлежащих области

# сначала заливаем 4 внутренних сегмента круга

# верхний правый
x = np.linspace(1, r * cos(1 / r), number_of_segments)
y = np.linspace(1, 1, number_of_segments)
y1 = np.cos(np.arcsin(x / r)) * r
plt.fill_between(x, y, y1, color=fill_color)

# нижний правый
x = np.linspace(1, r * cos(1 / r), number_of_segments)
y = np.linspace(-1, -1, number_of_segments)
y1 = -np.cos(np.arcsin(x / r)) * r
plt.fill_between(x, y, y1, color=fill_color)

# верхний левый
x = np.linspace(-r * cos(1 / r), -1, number_of_segments)
y = np.linspace(1, 1, number_of_segments)
y1 = np.cos(np.arcsin(x / r)) * r
plt.fill_between(x, y, y1, color=fill_color)

# нижний левый
x = np.linspace(-r * cos(1 / r), -1, number_of_segments)
y = np.linspace(-1, -1, number_of_segments)
y1 = -np.cos(np.arcsin(x / r)) * r
plt.fill_between(x, y, y1, color=fill_color)

# теперь рисуем части креста вне окружности

# верхний
x = np.linspace(-1, 1, number_of_segments)
y = np.linspace(5, 5, number_of_segments)
y1 = np.cos(np.arcsin(x / r)) * r
plt.fill_between(x, y, y1, color=fill_color)

# нижний
x = np.linspace(-1, 1, number_of_segments)
y = np.linspace(-5, -5, number_of_segments)
y1 = -np.cos(np.arcsin(x / r)) * r
plt.fill_between(x, y, y1, color=fill_color)

# верхний
x = np.linspace(-1, 1, number_of_segments)
y = np.linspace(5, 5, number_of_segments)
y1 = np.cos(np.arcsin(x / r)) * r
plt.fill_betweenx(x, y, y1, color=fill_color)

# нижний
x = np.linspace(-1, 1, number_of_segments)
y = np.linspace(-5, -5, number_of_segments)
y1 = -np.cos(np.arcsin(x / r)) * r
plt.fill_betweenx(x, y, y1, color=fill_color)

##########
# этап 4 #
##########
# рисуем точку
plt.plot(px, py, color=point_color, marker='o', markersize=10)

plt.show()