import sys

from log import log
from root_degree import root

def diffie_hellman(q, m, a, b):
    x = root(1, q**a, m)
    y = root(1, q**b, m)
    return root(1, y**a, m)

if (__name__ == '__main__' and len(sys.argv) > 4):
    q = int(sys.argv[1])
    m = int(sys.argv[2])

    a = int(sys.argv[3])
    b = int(sys.argv[4])

    print(diffie_hellman(q, m, a, b))
