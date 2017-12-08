# Проверить подлинность сообщения
def check(q, r, s):
    p, g, y = 337, 15, 303
    return (y**r * r**s) % p == pow(g, q, p)

if __name__ == '__main__':
    print(check(309, 31, 232))
    print(check(19, 31, 74))
    print(check(106, 31, 324))
    print(check(106, 185, 81))
    print(check(99, 187, 88))
