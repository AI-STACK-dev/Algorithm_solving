# n = int(input())
# times = [0] * (n+1)
# costs = [0] * (n+1)
# for i in range(1, n+1):
#     t, p = map(int, input().split())
#     times[i] = t
#     costs[i] = p

# dp = [0] * (n+1)
# for i in range(1, n+1):
#     for j in range(1, i):
#         if j + times[j] - 1 <= i:
#             dp[i] = max(dp[i], dp[j] + costs[j])
# print(dp)
# print(dp[-1])

n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0

for _ in range(n):
    x,y = map(int, input().split())
    t.append(x)
    p.append(y)

for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        print(p[i], dp[time])
        dp[i] = max(p[i] + dp[time], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value
    print(dp)
print(max_value)