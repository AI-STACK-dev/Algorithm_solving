import sys; input=sys.stdin.readline

n = int(input().rstrip())
data = [ int(input().rstrip()) for _ in range(n)]
dp = [0]*n

if n == 1:
    print(data[0])
    exit()
elif n == 2:
    print(data[0]+data[1])
    exit()

dp[0] = data[0]
dp[1] = data[0] + data[1]
dp[2] = max(data[0],data[1])+data[2]

for i in range(3,n):
    dp[i] = max(dp[i-3]+data[i-1],dp[i-2])+data[i]
print(dp[-1])