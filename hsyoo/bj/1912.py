import sys
n = int(input())
ary = list(map(int, sys.stdin.readline().rstrip().split()))
dp = [0] * (n)

dp[0] = ary[0]
for i in range(1,n):
    dp[i] = max(dp[i-1] + ary[i], ary[i])
print(max(dp))
