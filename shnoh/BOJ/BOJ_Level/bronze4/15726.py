import sys; input = sys.stdin.readline;
A, B, C = map(int, input().split())
res = int(max(A * B / C, A / B * C))
print(res)