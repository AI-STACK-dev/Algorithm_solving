n = int(input())
DP = [0] * (n + 1)
for i in range(1, n + 1):
    DP[i] = DP[i-1] + i
print(DP[n])