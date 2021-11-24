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

ans = ''
x,y = len(a),len(b)
while True:
    if len(ans) == dp[-1][-1]:
        print(ans)
        break
    if b[y-1] == a[x-1]:
        ans = b[y-1] + ans 
        x -= 1
        y -= 1
    else:
        if dp[y][x-1] > dp[y-1][x]:
            x -= 1
        else:
            y -= 1 