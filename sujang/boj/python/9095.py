import sys; input = sys.stdin.readline

t = int(input().rstrip())
data = [ int(input().rstrip()) for _ in range(t)]
mx = max(data)

dp = [0] * (mx + 1)

for i in range(1,mx+1):
    if i ==1:
        dp[i] = 1
    elif i ==2:
        dp[i] = 2
    elif i==3:
        dp[i] = 4
    else:
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for d in data:
    print(dp[d])
    
