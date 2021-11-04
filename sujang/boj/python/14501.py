from sys import stdin

n = int(stdin.readline().rstrip())
data = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]

dp = [0]*n
for i in range(n):
    t,p = data[i]
    if i ==0:
        prev = 0
    else:
        prev = dp[i-1] 
    if i+t-1 < n:
        dp[i+t-1] = max(prev+p,dp[i+t-1])
    dp[i] = max(prev,dp[i])
print(dp[-1])