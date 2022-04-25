import sys; input = sys.stdin.readline;
n, h, v = map(int, input().split())
x = max(v, n - v)
y = max(h, n - h)
print(x * y * 4)