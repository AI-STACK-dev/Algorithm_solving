t = int(input())
for _ in range(t):
    n = int(input())
    if n <= 3:
        dp = [0] * 4
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        print(dp[n])
    else:
        dp = [0] * 11
        dp[1] = 1
        dp[2] = 2
        dp[3] = 4
        for i in range(4, 11):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        print(dp[n])
        
