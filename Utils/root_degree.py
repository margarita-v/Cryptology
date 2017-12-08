# x^a = b (mod c)
# a, b, c is command line arguments

import sys

def root(a, b, c):
    for i in range(1, c):
        if ( pow(i, a, c) == b):
        #if ((i**a - b) % c == 0):
            return i
    return None

if (__name__ == '__main__' and len(sys.argv) > 3):
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])

    print(root(a, b, c))

