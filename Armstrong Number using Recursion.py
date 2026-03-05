def power_sum(n, digits):
    if n == 0:
        return 0
    return (n % 10) ** digits + power_sum(n // 10, digits)

num = 153
digits = len(str(num))

if num == power_sum(num, digits):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
