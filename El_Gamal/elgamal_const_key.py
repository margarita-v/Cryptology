# -*- coding: utf-8 -*-
# Для схемы шифрования Эль-Гамаля расшифровать сообщение Q2 от абонента А,
# при условии, что абонент А не менял сессионный ключ k.
import sys
sys.path.append('../')

from Utils.modular_inverse import modinv

def get_second_message(b1, b2, p, q1):
    return ( q1 * b2 * modinv(b1, p) ) % p

if __name__ == '__main__':
    p = 54751
    b1, b2, q1 = 50973, 4246, 123
    print(get_second_message(b1, b2, p, q1))
