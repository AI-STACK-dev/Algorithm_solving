import sys; input = sys.stdin.readline;
n = int(input())
data = list(map(int, input().split()))
m = int(input())
for _ in range(m):
    k, l, r = map(int, input().split())
    if k == 1:
        for i in range(l - 1, r):
            data[i] = data[i] ** 2 % 2010
    else:
        print(sum(data[l - 1: r]))