# Функция нахождения обратного элемента a^(-1) mod p
# p простое, a принадлежит [1, p-1]

# РАБОТАЕТ НЕВЕРНО
def inverse(a, p):
    u, v = a, p
    x1, x2 = 1, 0
    while u != 1 and v != 1:
        while u % 2 == 0:
            u = int(u / 2)
            if x1 % 2 == 0:
                x1 = int(x1 / 2)
            else:
                x1 = int((x1 + p) / 2)
        while v % 2 == 0:
            v = (v / 2)
            if x2 % 2 == 0:
                x2 = int(x2 / 2)
            else:
                x2 = int((x2 + p) / 2)
        if u >= v:
            u -= v
            x1 -= x2
        else:
            v -= u
            x2 -= x1
    return x1 % p if u == 1 else x2 % p
