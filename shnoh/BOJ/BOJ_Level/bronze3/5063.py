import sys; input = sys.stdin.readline;
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
for t in data:
    if t[0] > t[1] - t[2]:
        print("do not advertise")
    elif t[0] < t[1] - t[2]:
        print("advertise")
    else:
        print("does not matter")