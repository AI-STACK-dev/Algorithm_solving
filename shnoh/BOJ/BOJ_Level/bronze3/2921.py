import sys; input = sys.stdin.readline;
n = int(input())
DP = [0] * (n + 1)
for i in range(1,n + 1):
    DP[i] = DP[i - 1] + i * (i + 1) * 3 // 2
print(DP[n])