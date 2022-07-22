n = int(input())
ary = list(map(int, input().split()))
ary.reverse()

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if ary[j] < ary[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n - max(dp))