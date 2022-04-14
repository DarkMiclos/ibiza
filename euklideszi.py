def euklidesz_rec(a,b):
    if b!=0:
        return euklidesz_rec(b, a % b)
    return a

print(euklidesz_rec(6, 9))