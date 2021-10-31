from sys import stdin

n = int(stdin.readline().rstrip())
data = list(map(int,stdin.readline().rstrip().split()))

dp = [1]*len(data)

for i in range(1,len(data)):
    for j in range(i):
        if data[j] < data[i]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j] + 1
        
print(max(dp))