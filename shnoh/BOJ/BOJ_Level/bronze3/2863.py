import sys; input = sys.stdin.readline;
a, b = map(int, input().split())
c, d = map(int, input().split())
data = [c,d,b,a]
Max = 0
for i in range(4):
    temp = data[(i + 3) % 4] / data[i % 4] + data[(i + 2) % 4] / data[(i + 1) % 4]
    if Max < temp:
        res = i
        Max = temp
print(res)