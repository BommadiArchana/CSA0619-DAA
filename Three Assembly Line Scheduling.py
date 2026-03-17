import math

stations=[
[5,9,3],
[6,8,4],
[7,6,5]
]

transfer=[
[0,2,3],
[2,0,4],
[3,4,0]
]

n=3
dp=[[math.inf]*3 for _ in range(n)]

for j in range(3):
    dp[0][j]=stations[j][0]

for i in range(1,n):
    for j in range(3):
        for k in range(3):
            dp[i][j]=min(dp[i][j],
                         dp[i-1][k]+transfer[k][j]+stations[j][i])

print("Minimum Production Time:",min(dp[n-1]))
