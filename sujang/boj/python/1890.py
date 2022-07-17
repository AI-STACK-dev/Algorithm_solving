n = int(input())
field = [ list(map(int,input().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i==n-1 and j==n-1:
            break
        curr = field[i][j]
        if j + curr < n:
            dp[i][j+curr] += dp[i][j]
        if i + curr < n:
            dp[i+curr][j] += dp[i][j]
print(dp[n-1][n-1])