# -*- coding: utf-8 -*-
# Подписать сообщение цифровой подписью

import sys
sys.path.append('../')

from Utils.inversion import inverse


def get_sign(q, p, g, x, k):
    r = pow(g, k, p)
    s = ((q - x*r) * inverse(k, p - 1)) % (p - 1)
    return r, s


if __name__ == '__main__':
    q, p, g = 3, 23, 5
    x, k = 7, 5
    print(get_sign(q, p, g, x, k))
