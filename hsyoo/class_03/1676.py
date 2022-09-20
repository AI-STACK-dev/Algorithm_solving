n = int(input())

dp = [0] * (n+1)
dp[0] = 1
if n == 0:
    print(0)
else:
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = i * dp[i-1]
    # print(dp)
    s = str(dp[-1])
    answer = 0
    while s.endswith('0'):
        answer +=1
        s = s[:-1]
    print(answer)