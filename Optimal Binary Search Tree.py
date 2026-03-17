freq = [34, 8, 50]
n = len(freq)

cost = [[0]*n for _ in range(n)]

for i in range(n):
    cost[i][i] = freq[i]

for L in range(2, n+1):
    for i in range(n-L+1):
        j = i + L - 1
        cost[i][j] = float('inf')
        total = sum(freq[i:j+1])

        for r in range(i, j+1):
            c = total
            if r > i:
                c += cost[i][r-1]
            if r < j:
                c += cost[r+1][j]
            cost[i][j] = min(cost[i][j], c)

print("Optimal Cost =", cost[0][n-1])
