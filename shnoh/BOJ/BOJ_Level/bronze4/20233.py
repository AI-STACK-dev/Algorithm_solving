import sys; input = sys.stdin.readline;
data = [int(input()) for _ in range(5)]
i = max(data[4] - 30, 0)
j = max(data[4] - 45, 0)

res1 = data[0] + 21 * data[1] * i
res2 = data[2] + 21 * data[3] * j
print(res1, res2)