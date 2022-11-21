import sys; input = sys.stdin.readline;
n, m = map(int, input().split())
data = [0] * n
for i in range(m):
    a, b = map(int, input().split())
    data[a - 1] += 1
    data[b - 1] += 1
for cnt in data:
    print(cnt)