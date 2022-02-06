import sys;input = sys.stdin.readline
from copy import deepcopy as dp
n = int(input())
data = list(map(int,input().rstrip().split()))
dp = dp(data)
for i in range(1,n):
    for j in range(i):
        if data[j] < data[i]:
            if dp[j] + data[i] > dp[i]:
                dp[i] = dp[j] + data[i]
print(max(dp))