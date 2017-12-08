# Подписать сообщение цифровой подписью
from modular_inverse import modinv

def get_sign(q, p, g, x, k):
    r = pow(g, k, p)
    s = (q - x*r) * modinv(k, p - 1)
    return r, s

if __name__ == '__main__':
    q, p, g = 3, 23, 5
    x, k = 7, 5
    print(get_sign(q, p, g, x, k))
