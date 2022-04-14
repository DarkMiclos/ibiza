from operator import mod


def kinai_maradektetel(c, m):
    big_m = 1
    for i in range(len(m)):
        big_m *= m[i]
    x = 0
    for i in range(len(c)):
        Mi = big_m // m[i]
        yi = modInverse(Mi, m[i])
        x += c[i] * Mi * yi
    x = x % big_m
    return x

def modInverse(a, m): # multiplikatív inverz
    m0 = m
    x = 1
    y = 0
    if m == 1:
        return 0
    while a > 1:
        q = a//m # // egész osztás kell
        b = m
        m = a % m
        a = b
        b = y
        y = x - q * y
        x = b
    if x < 0:
        x += m0
    return x

c = [0, 1, 2]
m = [5, 3, 4]
print(kinai_maradektetel(c, m))