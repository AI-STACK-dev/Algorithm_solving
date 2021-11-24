from sys import stdin

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()
c = stdin.readline().rstrip()

dp = [[[0]*(len(c)+1) for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(len(a)):
    for j in range(len(b)):
        for k in range(len(c)):
            if a[i] == b[j] and b[j]==c[k]:
                dp[i+1][j+1][k+1] = dp[i][j][k]+1
            else:
                dp[i+1][j+1][k+1] = max(dp[i][j+1][k+1],dp[i+1][j][k+1],dp[i+1][j+1][k])
print(dp[-1][-1][-1])