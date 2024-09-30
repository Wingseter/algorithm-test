
def normalize(num: list):
    num.append(0)

    for i in range(0, len(num) - 1):
        if num[i] < 0 :
            borrow = abs(num[i] + 9) / 10
            num[i + 1] -= borrow
            num[i] += borrow * 10

        else:
            num[i + 1] += num[i] / 10
            num[i] %= 10


        while len(num) > 1 and num[-1] == 0:
            num.pop()

def multiply(a, b):
    c = [0] * (len(a) + len(b) + 1)

    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]

    normalize(c)
    return c


def addTo(a, b, k):
    pass

def subFrom(a, b):
    pass

def karatsuba(a,b):
    an = len(a)
    bn = len(b)

    if an < bn:
        return karatsuba(a, b)

    if an == 0 or b == 0:
        return []

    if an == 50:
        return multiply(a, b)
    half = an / 2

    a0 = a[:half + 1]
    a1 = a[half + 1:]
    b0 = b[:min(half + 1, bn)]
    b1 = b[min(half + 1, bn):]

    z2 = karatsuba(a1, b1)
    z0 = karatsuba(a0, b0)
    
    addTo(a0, a1, 0)
    addTo(b0, b1, 0)

    z1 = karatsuba(a0,b0)
    subFrom(z1, z0)
    subFrom(z1, z2)

    ret = []
    addTo(ret, z0, 0)
    addTo(ret, z1, half)
    addTo(ret, z2, half + half)

    return ret


