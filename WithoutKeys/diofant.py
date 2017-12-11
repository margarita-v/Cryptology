# -*- coding: utf-8 -*-

from math import gcd

import sys
sys.path.append('../')


# Найти решение (x0, y0) уравнения ax + by = c
def get_solve(a, b, c):
    # Коэффициенты уравнения должны быть взаимно простыми
    div = gcd(a, b)
    if div > 1:
        a //= div
        b //= div
        c //= div
    for i in range(1, b):
        if (a * i - c) % b == 0: 
            x = i
            y = (c - a*x) // b
            return x, y
    return None


# Найти m, зная следующие параметры:
def get_solve2(r, a, b, m1, m2):
    x, y = get_solve(a, b, 1)
    return pow(m1, x, r) * pow(m2, y, r)


if __name__ == '__main__':
    a, b, c = 69, 273, 6
    print(get_solve(69, 273, 6))
