def is_prime(n, i=2):
    if i * i > n:
        return n > 1
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

num = 11
if is_prime(num):
    print("Prime Number")
else:
    print("Not Prime Number")
