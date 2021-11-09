import sys
DP = [[0] * 15 for _ in range(15)]
for i in range(1,15):
    DP[0][i] = i
for i in range(1,15):
    for j in range(1,15):
        DP[i][j] = DP[i - 1][j] + DP[i][j - 1]

t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    print(DP[k][n])
