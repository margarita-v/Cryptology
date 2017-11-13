# -*- coding: utf-8 -*-
# По открытому ключу найти секретный
# (m, q, x, y)

for a in (2, 10000):
    t = q**a
    if (x % m) == (t % m):
        print(a)
        break
