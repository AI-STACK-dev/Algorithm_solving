import sys; input = sys.stdin.readline;
x, y = map(int, input().split())
x = x - 1
y = y - 1
x1 = x // 4
x2 = x % 4
y1 = y // 4
y2 = y % 4
print(abs(x1 - y1) + abs(x2 - y2))