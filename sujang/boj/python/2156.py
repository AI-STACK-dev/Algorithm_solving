import sys; input = sys.stdin.readline

n = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(n)]

dp = [0]*(n)
for i in range(n):
    if i==0:
        dp[i] = data[i]
    elif i==1:
        dp[i] = data[i-1]+data[i]
    elif i ==2:
        dp[i] = max(dp[i-1],data[i-1]+data[i], data[i-2]+data[i])
    else:
        dp[i] = max(dp[i-1],dp[i-2]+data[i], dp[i-3]+data[i-1]+data[i])
print(dp[n-1])