import sys; input = sys.stdin.readline;
T = int(input())
DP = [1] * 301
DP2 = [3] * 301
res = 0
for i in range(1, 301):
    DP[i] = DP[i - 1] + i + 1
for i in range(1, 300):
    DP2[i] = DP2[i - 1] + DP[i + 1] * (i + 1)
for _ in range(T):
    n = int(input())
    print(DP2[n - 1])