# Проверить подлинность сообщения
def check(p, g, y, q, r, s):
    return (y**r * r**s) % p == pow(g, q, p)

if __name__ == '__main__':
    p, g, y = 337, 15, 303
    print(check(p, g, y, 309, 31, 232))
    print(check(p, g, y, 19, 31, 74))
    print(check(p, g, y, 106, 31, 324))
    print(check(p, g, y, 106, 185, 81))
    print(check(p, g, y, 99, 187, 88))
