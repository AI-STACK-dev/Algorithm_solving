import sys; input = sys.stdin.readline;
N, m, M, T, R = map(int, input().split())
res = 0
cur = m
if M - m < T:
    print(-1)
else:
    while N > 0:
        res += 1
        if cur + T <= M:
            cur += T
            N -= 1
        else:
            cur -= R
            if cur < m:
                cur = m
    print(res)