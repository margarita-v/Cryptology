def check_abonent(p, q, g, y, r, s, e):
    result = r == (g**s * y ** e) % p
    # find secret key if result is True
    return result

p = 33107
q = 16553
g = 2902
y = 9107
r = 32607

if __name__ == '__main__':
    print(check_abonent(p, q, g, y, r, 9856, 15776))
    print(check_abonent(p, q, g, y, r, 8108, 490))
    print(check_abonent(p, q, g, y, r, 7309, 9987))
    print(check_abonent(p, q, g, y, r, 1267, 155))
