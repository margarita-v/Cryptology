# -*- coding: utf-8 -*-
"""Условие задачи:
    Алгоритм Эль-Гамаля. Боб получил от Алисы сообщение Q = 23605
    с электронной подписью (r, s) = (54822, 44475).
    Открытый ключ: (p, g, y) = (80207, 38750, 42999).
    Может ли Боб считать сообщение подлинным?"""

import sys
sys.path.append('../')

from El_Gamal.elgamal_check import check


q, r, s = 23605, 54822, 44475
p, g, y = 80207, 38750, 42999
print(check(p, g, y, q, r, s))
