def knapsack(weight, values, cap):
    n = len(values)
    dp = [[0]*(cap+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(cap+1):
            if weight[i -1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1]+dp[i-1][w-weight[i-1]])
                
            else:
                dp[i][w] = dp[i-1][w]
    return dp[n][cap]

values = [60,100,120]
weight = [10,20,30] 
print(knapsack(weight, values, 50))