def dice_throw(num_dice, num_sides, target):
    dp = [[0]*(target+1) for _ in range(num_dice+1)]
    dp[0][0] = 1

    for i in range(1, num_dice+1):
        for j in range(1, target+1):
            for k in range(1, num_sides+1):
                if j-k >= 0:
                    dp[i][j] += dp[i-1][j-k]

    return dp[num_dice][target]

print("Test Case 1:", dice_throw(2,6,7))
print("Test Case 2:", dice_throw(3,4,10))
