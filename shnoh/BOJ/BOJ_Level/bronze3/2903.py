import sys; input = sys.stdin.readline;
dp = [2] * 16
n = int(input())
for i in range(1, n + 1):
    dp[i] = 2 * dp[i - 1] - 1
print(dp[n] ** 2)