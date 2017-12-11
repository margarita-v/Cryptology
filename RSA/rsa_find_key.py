# -*- coding: utf-8 -*-
# Найти секретный ключ абонента А

import sys
sys.path.append('../')

from Utils.phi import phi_new
from Utils.inversion import inverse


def rsa_key(r, a):
    euler = phi_new(r)
    return inverse(a, euler)


def euler_brut(r, a):
    euler = phi_new(r)
    for i in range(euler, 0, -1):
        if (a * i - 1) % euler == 0:
            return i


if __name__ == '__main__':
    r, a = 66899179, 9467
    print(rsa_key(r, a))
