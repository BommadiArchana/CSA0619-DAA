def maxCoins(piles):
    piles.sort()
    n = len(piles)//3
    i = len(piles)-2
    ans = 0
    
    for _ in range(n):
        ans += piles[i]
        i -= 2
        
    return ans

print(maxCoins([2,4,1,2,7,8]))
print(maxCoins([2,4,5]))
