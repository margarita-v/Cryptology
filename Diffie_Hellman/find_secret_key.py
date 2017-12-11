# Diffie-Hellman

import sys
sys.path.append('../')

from Utils.log import log


def find_key(q, m, a, b):
    x = pow(q, a, m)
    y = pow(q, b, m)

    k1 = pow(y, a, m)
    k2 = pow(x, b, m)
    # k1 = k2
    return k1


# Find secret key using opened key
def hack(q, m, x, y):
    a = log(q, x, m)
    b = log(q, y, m)
    return pow(y, a, m)


if __name__ == '__main__':
    q, m = 11, 67
    a, b = 47, 51
    print(find_key(q, m, a, b))
    m, q, x, y = 4397, 2381, 2567, 1109
    print(hack(q, m, x, y))
