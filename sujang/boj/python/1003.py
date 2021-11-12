import sys; input = sys.stdin.readline

data = []
for _ in range(int(input())):
    data.append(int(input()))

m = max(data)
dp = [[0,0] for _ in range(m+1)]

for i in range(m+1):
    if i == 0:
        dp[i][0] = 1
    elif i ==1:
        dp[i][1] = 1
    else:
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

for d in data:
    print(*dp[d])