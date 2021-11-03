from sys import stdin

n = int(stdin.readline().rstrip())

dp = [0]*(n+1)
track = [0]*(n+1)

for i in range(2,n+1):
    track[i] = i-1
    dp[i] = dp[i-1]+1
    if i%2==0:
        if dp[i] > dp[i//2]+1:
            dp[i] = dp[i//2]+1
            track[i] = i//2
    if i%3==0:
        if dp[i] > dp[i//3]+1:
            dp[i] = dp[i//3]+1
            track[i] = i//3

ans = []
while n != 1:
    x = track[n]
    ans.append(n)
    n = x
ans.append(1)
print(len(ans)-1)
print(*ans)

