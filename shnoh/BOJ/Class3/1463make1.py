import sys; input = sys.stdin.readline;

n = int(input())
DP = [n] * (n + 3)
DP[1] = 0
DP[2] = 1
DP[3] = 1
for i in range(4, n + 1):
    if i % 3 == 0:
        DP[i] = min(DP[i], DP[i // 3] + 1)
    if i % 2 == 0:
        DP[i] = min(DP[i], DP[i // 2] + 1)
    DP[i] = min(DP[i], DP[i - 1] + 1)
print(DP[n])
