from math import sqrt
import sys; input = sys.stdin.readline
n = int(input())
dp = list(range(n+1))
for i in range(2,n+1):
    if i == int(sqrt(i))**2:
        dp[i] = 1
    else:
        for j in range(1,int(sqrt(i))+1):
            dp[i] = min(dp[i],dp[j**2]+dp[i-j**2])
print(dp[-1])