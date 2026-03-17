arr = [10, 45, 2, 78, 23]

largest = arr[0]
for num in arr:
    if num > largest:
        largest = num

print("Largest Element:", largest)
