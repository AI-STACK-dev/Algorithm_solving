from sys import stdin

n = int(stdin.readline().rstrip())

dp = [0]*(n+1)
dp[0] = 1
dp[1] = 3
for i in range(2,n):
    dp[i] = (dp[i-2]*2 + dp[i-1])%10007
print(dp[n-1])