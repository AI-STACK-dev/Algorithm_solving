from sys import stdin

a = stdin.readline().rstrip()
b = stdin.readline().rstrip()

dp = [[0]*(len(a)+1) for _ in range(len(b)+1)]

for i in range(len(b)):
    for j in range(len(a)):
        if b[i] == a[j]:
            dp[i+1][j+1] = dp[i][j]+1
        else:
            dp[i+1][j+1] = max(dp[i+1][j],dp[i][j+1])
print(dp[-1][-1])


