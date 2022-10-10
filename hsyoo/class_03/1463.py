x = int(input())
INF = int(1e9)
dp = [INF] * (x+1)

if x == 1:
    print(0)
else:
    dp[1] = 0
    for i in range(2, x+1):
        # print(dp)
        min_ = INF
        if i % 3 == 0:
            min_ = min(min_, dp[i//3] + 1)
        if i % 2 == 0:
            min_ = min(min_, dp[i//2] + 1)
        
        min_ = min(min_, dp[i-1] + 1)
        dp[i] = min_
    print(dp[x])