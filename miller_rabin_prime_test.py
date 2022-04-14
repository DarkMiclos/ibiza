import random

def miller_rabin_test(n, m):
    a = random.randint(2, n-2)
    x = gyorshatvanyozas(a, m, n)
    if(x == 1 or x == n-1):
        return True
    while(m != n-1):
        x = (x ** 2) % n
        m = m * 2
        if(x == 1):
            return False
        if(x == n-1):
            return True
    return False

def gyorshatvanyozas(a, b, m):
    result = 1
    apow = a
    while(b != 0):
        if b & 0x01 == 0x01:
            result = (result * apow) % m
        b >>= 1
        apow = (apow * apow) % m
    return result

print("cia")
print(miller_rabin_test(197, 7))