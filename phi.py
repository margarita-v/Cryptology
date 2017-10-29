# -*- coding: utf-8 -*-
import fractions
from math import sqrt

# Функция, проверяющая, является ли число простым
def isPrime(n):
    if (n < 2):
        return False
    for i in range(2, int(sqrt(n) + 1)):
        if (n % i == 0):
            return False
    return True

# Функция, вычисляющая значение функции Эйлера
# Если n > 0, то phi(n) равно количеству чисел, взаимно простых с n,
# в диапазоне от 1 до n.
# 1 <= k <= n : gcd(n, k) = 1
def phi(n):
    if (isPrime(n)):
        return n - 1
    count = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            count += 1
    return count

def phi_improved(n):
    if (isPrime(n)):
        return n - 1
    # Находим делители числа n
    dividers = []
    for i in range(2, int(sqrt(n))):
        if (n % i == 0):
            dividers.append((i, int(n / i)))
    result = n
    # Проверяем, что делители простые, и находим значение функции Эйлера
    for div in dividers:
        #print(div[0], ' ', div[1])
        if (isPrime(div[0])):
            result *= (1 - 1/div[0])
        if (isPrime(div[1])):
            result *= (1 - 1/div[1])
    return result
