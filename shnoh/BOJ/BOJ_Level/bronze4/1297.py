import sys; input = sys.stdin.readline;
D, H, W = map(int, input().split())
# 9x^2 + 16x^2 = 52^2
# (a^2 + b^2)x^2 = c^2
# ax, bx
x = (D ** 2 / ( H ** 2 + W ** 2)) ** 0.5
print(int(H * x), int(W * x))