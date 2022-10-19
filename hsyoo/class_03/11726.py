import sys

n = int(sys.stdin.readline())
dp = [1,2]+[0]*(n-2)

for i in range(2,n):
    dp[i] = dp[i-1] + dp[i-2]
        
print(dp[n-1] % 10007)