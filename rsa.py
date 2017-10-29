from phi import phi, phi_improved, isPrime
from modular_inverse import modinv

def rsa_key(r, a):
    return modinv(a, int(phi(r)))

def euler_brut(r, a):
    euler = int(phi_improved(r))
    for i in range(euler, 0, -1):
        if (a * i - 1) % euler == 0:
            return i

r, a = 66899179, 9467
print(rsa_key(r, a))
#print(euler_brut(r, a))
