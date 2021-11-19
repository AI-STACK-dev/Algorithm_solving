import sys; input = sys.stdin.readline

b = int(input().rstrip())
n = int(input().rstrip())

sum = [0]*(n+1)
expo = [0]*(n+1)
dp = [ [0]*(b+1) for _ in range(n+1)]

for i in range(1,n+1):
    d = int(input().rstrip())
    sum[i] = sum[i-1] + d
    expo[i] = expo[i-1] + d**2
    for j in range(b+1):
        dp[i][j] = int(1e9)

for i in range(1,n+1):
    for j in range(1,b+1):
        for k in range(i):
            if dp[k][j-1] == int(1e9):
                continue
            avg = (sum[i] - sum[k]) / (i-k)
            error = (expo[i] - expo[k]) - 2 * avg * (sum[i]-sum[k]) + (avg**2) * (i-k)
            dp[i][j] = min(dp[i][j], dp[k][j-1] + error)

print(round(dp[n][b],6)) 