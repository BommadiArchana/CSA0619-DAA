p = [1,2,3,4]
n = len(p) - 1

m = [[0]*n for _ in range(n)]

for L in range(2, n+1):
    for i in range(n-L+1):
        j = i + L - 1
        m[i][j] = float('inf')
        for k in range(i, j):
            q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
            m[i][j] = min(m[i][j], q)

print("Minimum Cost =", m[0][n-1])
