# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
import fractions    # можно реализовать и без этого модуля, но тогда коэффициенты будут некрасивые, либо код длинный
x1 = int(input('Введите x1'))
y1 = int(input('Введите y1'))
x2 = int(input('Введите x2'))
y2 = int(input('Введите y2'))

# Вычисляем числитель и знаменатель канонического выражения
# x - x1   y - y1
# ------ = ------
# x2 - x1  y2 - y1

kx1 = 0 - x1
kx2 = x2 - x1
ky1 = 0 - y1
ky2 = y2 - y1
# ky2 * (x + kx1) = kx2 * (y + ky1)

k = fractions.Fraction(ky2, kx2)
b2_1 = fractions.Fraction(ky2 * kx1, kx2)
b2_2 = fractions.Fraction(ky1, 1)
b = b2_1 - b2_2
print(f'y = {k}x + {b}')
