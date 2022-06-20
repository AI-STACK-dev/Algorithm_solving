import sys; input = sys.stdin.readline;
n, w, h = map(int, input().split())
d = (w**2 + h**2) ** 0.5
for i in range(n):
    if int(input()) <= d:
        print("DA")
    else:
        print("NE")