from sys import stdin

st1 = stdin.readline().rstrip()
st2 = stdin.readline().rstrip()

dp = [[0]*(len(st1)+1) for _ in range(len(st2)+1)]

# 초기값 설정
for i in range(len(st1)+1):
    dp[0][i] = i
for i in range(len(st2)+1):
    dp[i][0] = i

# dp 테이블 채우기
for i in range(1,len(st2)+1):
    for j in range(1,len(st1)+1):
        if st1[j-1]==st2[i-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
print(dp[-1][-1])