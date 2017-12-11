# -*- coding: utf-8 -*-
# Расшифровать сообщение m через k итераций

import sys
sys.path.append('../')


def get_count(r, a, c):
    mult = c ** a
    k = 1
    while pow(mult, k, r) != c:
        k += 1
    return k


if __name__ == '__main__':
    r = 212887
    a = 3061
    c = 35947
    # Количество итераций
    k = get_count(r, a, c)
    print('k =', k)
    # Исходное сообщение
    m = pow(c, k, r)
    print('m =', m)
