def rob(arr, i = 0):
    dp = [0 for i in range(len(arr))]
    dp[0] = arr[0]
    dp[1] = max(dp[0], arr[1])
    for i in range(2, len(arr)):
        dp[i] = max(arr[i] + dp[i-2], dp[i-1])

    return dp[len(arr)-1]
print(rob([4,8,12,1,2,10,3,6,8]))