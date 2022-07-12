import sys; input = sys.stdin.readline

n,s,m = map(int,input().split())
data = list(map(int, input().split()))

dp = [[0]*(m+1) for _ in range(n+1)]
dp[0][s] = 1

for i in range(1,n+1):
    for j in range(m+1):
        if dp[i-1][j] == 1:
            if 0<=j+data[i-1]<=m:
                dp[i][j+data[i-1]] = 1
            if 0<=j-data[i-1]<=m:
                dp[i][j-data[i-1]] = 1

ans = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        ans = i
        break
print(ans)
