import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    cnt = 0
    for a in range(1, n - 1):
        for b in range(a + 1, n):
            if not ( a ** 2 + b ** 2 + m) % (a * b):
                cnt += 1
    print(cnt)