import sys; input = sys.stdin.readline;
n, w, h = map(int, input().split())
d = (w ** 2 + h ** 2) ** 0.5
for _ in range(n):
    m = int(input())
    if m > d:
        print("NO")
    else:
        print("YES")