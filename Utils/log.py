# a^x = b (mod c)


def log(a, b, c):
    for i in range(1, c):
        if pow(a, i, c) == b:
            return i
    return None


if __name__ == '__main__':
    a, b, c = 270, 342, 503
    print(log(a, b, c))
