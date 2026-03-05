num = 28
sum_div = 0

for i in range(1, num//2 + 1):
    if num % i == 0:
        sum_div += i

if sum_div == num:
    print("Perfect Number")
else:
    print("Not Perfect Number")
