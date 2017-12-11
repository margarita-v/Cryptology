# -*- coding: utf-8 -*-
# Найти открытый ключ и зашифровать слово "why"

import sys
sys.path.append('../')

from Utils.inversion import inverse


def find_key(inc_list, q, r):
    result = []
    for w in inc_list:
        result.append( (r*w) % q)
    return result


def encrypt(message, key):
    #for char in message:
     #   m = format(char, 'b')
    print(list(format(25, 'b')))


# Расшифровка сообщения
def solve():
    w = [1, 2, 4, 9, 18, 35]
    q, r = 80, 29

    #text = [55, 97, 21, 79, 100, 155]
    text = [42, 79, 78, 97, 154, 57]

    # Отнимаем единицу, так как индексация идет с нуля
    n = len(w) - 1 # Длина ключа
    k = len(text) - 1 # Длина шифротекста

    inverse_elem = inverse(r, q)
    s = [i * inverse_elem % q for i in text]

    matrix = [[0 for i in range(k + 1)] for j in range(n + 1)]
    m = [0 for i in range(k + 1)]
    for j in range(k + 1):
        for i in range(0, n):
            index = n - i
            matrix[j][index] = 0 if w[index] > s[j] else 1
            s[j] -= matrix[j][index] * w[index]
        for i in range(1, n + 1):
            m[j] += matrix[j][i] * 2**(n - i)
    print(m)


if __name__ == '__main__':
    key = find_key([2, 3, 7, 15, 31], 61, 17)
    solve()
