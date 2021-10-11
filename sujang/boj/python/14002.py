from sys import stdin

n = int(stdin.readline())
data = list(map(int,stdin.readline().split()))

dp = [1 for i in range(n)]
array = [[x] for x in data]


for i in range(n):
    for j in range(i):
        if data[i] > data[j]:
            if dp[i] < dp[j]+1:
                array[i] = array[j] + [data[i]]
                dp[i] = dp[j] + 1

length = 0
idx = 0
for i in range(n):
    if dp[i] > length:
        length = dp[i]
        idx = i
print(length)
print(*array[idx])
