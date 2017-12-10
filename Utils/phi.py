# -*- coding: utf-8 -*-
import fractions
from math import sqrt

from sympy.ntheory import factorint

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
    if (is_prime(n)):
        return n - 1
    count = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            count += 1
    return count

# Функция Эйлера (лучший алгоритм из представленных)
def phi_new(n):
    dividers = factorint(n)
    if (len(dividers) == 1):
        return n - 1
    result = n
    for key, value in dividers.items():
        result *= get_multiplier(key)
    return int(result)

def phi_f(val):
    res = val
    i = 2
    for i in range(2, val + 1):
        if val % i == 0:
            res *= 1 - 1 / i
            while val % i == 0:
                val /= i
    return int(res)

def phi_improved(n):
    dividers = get_dividers(n)
    if (is_empty(dividers)):
        return n - 1
    # Находим делители числа n
    print(dividers)
    result = n
    # Проверяем, что делители простые, и находим значение функции Эйлера
    for div in dividers:
        if (is_prime(div[0])):
            result *= get_multiplier(div[0])
        if (is_prime(div[1])):
            result *= get_multiplier(div[1])
    return result

# Функция, проверяющая, является ли число простым
def is_prime(num):
    return is_empty(get_dividers(num))

def is_empty(dividers):
    return len(dividers) == 0

def get_multiplier(num):
    return 1 - 1 / num
