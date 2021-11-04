from sys import stdin
import math

n = int(stdin.readline().rstrip())
data = list(map(int,stdin.readline().rstrip().split()))

dp = [1]*n

for i in range(1,n):
    for j in range(i):
        if data[j] > data[i] and dp[i] < dp[j]+1:
            dp[i] = dp[j]+1
print(n-max(dp))
