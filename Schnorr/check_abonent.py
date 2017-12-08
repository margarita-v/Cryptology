# -*- coding: utf-8 -*-
# Протокол аутентификации Шнорра (Schnorr)
# Мы - абонент B. Проверить, что мы общаемся с абонентом A.
import sys
sys.path.append('../')

from Utils.modular_inverse import modinv
from Utils.log import log

def check_abonent(r, g, y, p, s, e):
    return r == (g**s * y ** e) % p

p = 33107
q = 16553
g = 2902
y = 9107
r = 32607

if __name__ == '__main__':
    print(check_abonent(r, g, y, p, 9856, 15776))
    print(check_abonent(r, g, y, p, 8108, 490))
    print(check_abonent(r, g, y, p, 7309, 9987))
    print(check_abonent(r, g, y, p, 1267, 155))

    # find secret key
    inverse_elem = modinv(g, p)
    print(inverse_elem)
    # find a
    a = log(g, r, p)
    print(a)
    #print( (s - a) * modinv(e, p))
