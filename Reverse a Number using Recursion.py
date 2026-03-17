def reverse(n, rev=0):
    if n == 0:
        return rev
    return reverse(n//10, rev*10 + n%10)

num = 1234
print("Reversed =", reverse(num))
