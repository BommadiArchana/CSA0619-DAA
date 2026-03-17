import sys

keys=[10,12,16,21]
freq=[4,2,6,3]

n=len(keys)

cost=[[0]*n for _ in range(n)]

for i in range(n):
    cost[i][i]=freq[i]

for L in range(2,n+1):
    for i in range(n-L+1):
        j=i+L-1
        cost[i][j]=sys.maxsize
        s=sum(freq[i:j+1])

        for r in range(i,j+1):
            c=(cost[i][r-1] if r>i else 0)+ \
              (cost[r+1][j] if r<j else 0)+s
            cost[i][j]=min(cost[i][j],c)

print("Optimal Cost:",cost[0][n-1])
