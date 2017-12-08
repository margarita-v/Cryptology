# a^x = b (mod c)
# a, b, c is command line arguments

import sys

def log(a, b, c):
    for i in range(1, c):
        if (pow(a, i, c) == b):
        #if ((a**i - b) % c == 0):
            return i
    return None

if (__name__ == '__main__' and len(sys.argv) > 3):
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    print(log(a, b, c))

