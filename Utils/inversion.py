# -*- coding: utf-8 -*-
# Функция нахождения обратного элемента a^(-1) mod p
# p простое, a принадлежит [1, p-1]


def inverse(a, p):
    cur = 0
    i = 0
    while cur != 1:
        cur += a
        cur %= p
        i += 1
    return i
