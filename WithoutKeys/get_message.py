# -*- coding: utf-8 -*-
'''Условие задачи:
    Для шифрования используется криптосистема без передачи ключей.
    Задан открытый ключ p, сообщение m зашифровано с помощью m1, m2, m3.
    Найти m.'''

import sys
sys.path.append('../')

from Utils.phi import phi_new
from Utils.log import log

def get_message(m1, m2, m3, p):
    phi = phi_new(p)
    b = log(m1, m2, p)
    for i in range(1, phi):
        if (b * i - 1) % phi == 0:
            return pow(m3, i, p)
    return None

if (__name__ == '__main__'):
    print('Контрольная работа, вариант 1:')
    p = 49559
    m1, m2, m3 = 11039, 31214, 14790
    print(get_message(m1, m2, m3, p))

    print('Контрольная работа, вариант 2:')
    p = 33569
    m1, m2, m3 = 15642, 1874, 25796
    print(get_message(m1, m2, m3, p))
