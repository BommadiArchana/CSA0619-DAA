def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

a = 48
b = 18
print("GCD =", gcd(a, b))
