import sys

keys = ['A','B','C','D']
freq = [0.1,0.2,0.4,0.3]

n = len(keys)

cost = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    cost[i][i+1] = freq[i]

for L in range(2,n+1):
    for i in range(n-L+1):
        j = i + L
        cost[i][j] = sys.maxsize
        total = sum(freq[i:j])
        for r in range(i,j):
            c = cost[i][r] + cost[r+1][j] + total
            cost[i][j] = min(cost[i][j], c)

print("Optimal Cost:", cost[0][n])
