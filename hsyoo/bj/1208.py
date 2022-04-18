n,s = map(int, input().split())
ary = list(map(int, input().split()))
dp = [0] * (n)
dp[0] = ary[0]
sum = 0
for i in range(1, n):
    dp[i-1]  = dp[i-1] + ary[i]

ans = 0
for i in range(1, n):
    for j in range(i):
        if dp[i] - dp[j-1] == s:
            ans += 1
print(ans)
