# -*- coding: utf-8 -*-
# Найти секретный ключ абонента А
import sys
sys.path.append('../')

from Utils.phi import phi, phi_improved
#from Utils.modular_inverse import modinv
from Utils.inversion import inverse

r, a = 66899179, 9467
euler = int(phi_improved(r))

def rsa_key(r, a):
    return inverse(a, euler)

def euler_brut(r, a):
    for i in range(euler, 0, -1):
        if (a * i - 1) % euler == 0:
            return i

if __name__ == '__main__':
    print(rsa_key(r, a))
