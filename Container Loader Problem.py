weights = [10, 20, 30]
capacity = 50
total = 0

for w in weights:
    if w <= capacity:
        capacity -= w
        total += w

print("Total loaded weight =", total)
