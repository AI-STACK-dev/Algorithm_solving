from sys import stdin

INF = int(1e9)
n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
dp = [[INF]*n for _ in range(n)]

# 대각성분 초기화
for i in range(n):
    dp[i][i] = 0

# data 받기
for _ in range(m):
    a,b,c = map(int,stdin.readline().rstrip().split())
    if dp[a-1][b-1] > c:
        dp[a-1][b-1] = c

# 플로이드 워셜 알고리즘
for a in range(n):
    for b in range(n):
        for c in range(n):
            dp[b][c] = min(dp[b][c], dp[b][a]+dp[a][c])

for a in range(n):
    for b in range(n):
        if dp[a][b] == INF:
            dp[a][b] = 0

for i in range(n):
    print(*dp[i])