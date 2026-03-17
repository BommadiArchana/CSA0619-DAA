n = 3
count = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            count += 1

print("Total Operations:", count)
print("Time Complexity: O(n^3)")
