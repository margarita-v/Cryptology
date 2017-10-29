# Iterative Algorithm
def iterative_egcd(a, b):
    x, y = 0, 1
    u, v = 1, 0
    while a != 0:
        q, r = b//a, b%a
        m, n = x - u*q, y - v*q # use x//y for floor "floor division"
        b, a = a, r 
        x, y = u, v
        u, v = m, n
    return b, x, y
 
# Recursive Algorithm
def recursive_egcd(a, b):
    """Returns a triple (g, x, y), such that ax + by = g = gcd(a,b).
       Assumes a, b >= 0, and that at least one of them is > 0.
       Bounds on output values: |x|, |y| <= max(a, b)."""
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = recursive_egcd(b % a, a)
        return (g, x - (b // a) * y, y)
 
egcd = iterative_egcd
 
def modinv(a, m):
    g, x, y = egcd(a, m) 
    if g != 1:
        return None
    else:
        return x % m
