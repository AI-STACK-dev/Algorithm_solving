import sys; input = sys.stdin.readline;
cur = 0
Max = 0
for _ in range(4):
    a, b = map(int, input().split())
    temp = cur
    cur += b - a
    Max = max(cur, Max)
print(Max)