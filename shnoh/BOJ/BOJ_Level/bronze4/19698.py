import sys; input = sys.stdin.readline;
N, W, H, L = map(int, input().split())

x = W // L
y = H // L
res = min(x * y, N)
print(res)