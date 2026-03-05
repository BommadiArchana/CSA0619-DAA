def factors(n, i=1):
    if i > n:
        return
    if n % i == 0:
        print(i, end=" ")
    factors(n, i+1)

factors(12)
