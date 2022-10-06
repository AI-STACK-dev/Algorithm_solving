import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    cnt = 0
    n, d = map(int, input().split())
    for _ in range(n):
        v, f, c = map(int, input().split())
        if v * f >= d * c:
            cnt += 1
    print(cnt)