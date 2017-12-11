# x^a = b (mod c)


def root(a, b, c):
    for i in range(1, c):
        if pow(i, a, c) == b:
            return i
    return None


if __name__ == '__main__':
    a, b, c = 7, 211, 317
    print(root(a, b, c))
