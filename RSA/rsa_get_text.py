# -*- coding: utf-8 -*-
# Для абонента B расшифровать полученное сообщение


def solve(m1, r, b, beta):
    print(pow(m1, beta, r))

    # Оптимизация вычислений
    beta1 = (beta - 1) // 10
    x = pow(m1, beta1, r)
    m = (x**10 * m1) % r
    print(m)


m1, r, b, beta = 25963634, 71361259, 74671, 33289711
solve(m1, r, b, beta)

print("Контрольная работа, вариант 1:")
m1, r, b, beta = 18701373, 32015873, 174673, 26803117
print(pow(m1, beta, r))
