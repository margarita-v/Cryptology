# -*- coding: utf-8 -*-
import fractions
from math import sqrt

# Функция, возвращающая список делителей числа
def get_dividers(n):
    result = []
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i == 0):
            result.append((i, n // i))
    return result

# Функция, вычисляющая значение функции Эйлера
# Если n > 0, то phi(n) равно количеству чисел, взаимно простых с n,
# в диапазоне от 1 до n.
# 1 <= k <= n : gcd(n, k) = 1
def phi(n):
    if (len(get_dividers(n)) == 0):
        return n - 1
    count = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            count += 1
    return count

def phi_improved(n):
    dividers = get_dividers(n)
    if (len(dividers) == 0):
        return n - 1
    # Находим делители числа n
    print(dividers)
    result = n
    # Проверяем, что делители простые, и находим значение функции Эйлера
    for div in dividers:
        if (len(get_dividers(div[0])) == 0):
            result *= (1 - 1/div[0])
        if (len(get_dividers(div[1])) == 0):
            result *= (1 - 1/div[1])
    return result
