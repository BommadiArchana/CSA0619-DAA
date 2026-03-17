import sys

dist = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

N = 4
dp = {}

def tsp(mask, pos):
    if mask == (1<<N)-1:
        return dist[pos][0]

    if (mask, pos) in dp:
        return dp[(mask, pos)]

    ans = sys.maxsize
    for city in range(N):
        if mask & (1<<city) == 0:
            ans = min(ans, dist[pos][city] + tsp(mask | (1<<city), city))

    dp[(mask, pos)] = ans
    return ans

print("Minimum Cost =", tsp(1,0))
