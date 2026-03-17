def pattern(n, i=1):
    if i > n:
        return
    print(*range(1, i+1))
    pattern(n, i+1)

pattern(4)
