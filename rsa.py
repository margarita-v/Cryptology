from phi import phi, phi_improved, isPrime
from modular_inverse import modinv

r, a = 66899179, 9467
euler = int(phi_improved(r))

def rsa_key(r, a):
    return modinv(a, euler)

def euler_brut(r, a):
    for i in range(euler, 0, -1):
        if (a * i - 1) % euler == 0:
            return i

if __name__ == '__main__':
    print(rsa_key(r, a))
    #print(euler_brut(r, a))
