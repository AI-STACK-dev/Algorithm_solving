n = int(input())
ary = list(map(int, input().split()))
ary.sort()
dp = [0] * (n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1] + ary[i-1]
print(sum(dp))