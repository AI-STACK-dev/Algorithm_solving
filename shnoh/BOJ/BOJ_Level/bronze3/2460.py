import sys; input = sys.stdin.readline;
data = [list(map(int, input().split())) for _ in range(10)]
Max = 0
cur = 0
for i in range(10):
    cur += data[i][1] - data[i][0]
    if cur > Max:
        Max = cur
print(Max)