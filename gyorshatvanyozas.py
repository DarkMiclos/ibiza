def gyorshatvanyozas(a, b, m):
    result = 1
    apow = a
    while(b != 0):
        if b & 0x01 == 0x01:
            result = (result * apow) % m
        b >>= 1
        apow = (apow * apow) % m
    return result

print(gyorshatvanyozas(5, 349, 29))