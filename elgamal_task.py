# Вычислить шифротекст и найти секретный ключ x
from log import log

def get_text(p, g, y, k, q):
    a = pow(g, k, p)
    b = (q* y**k) % p
    return a, b

def find_key(y, g, p):
    return log(g, y, p)

if __name__ == '__main__':
    p, g, y = 23, 5, 14
    k, q = 16, 20
    print(get_text(p, g, y, k, q))
    print(find_key(y, g, p))
