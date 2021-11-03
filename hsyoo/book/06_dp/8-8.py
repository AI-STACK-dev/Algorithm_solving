import sys
n, m = map(int, input().split())
ary = []
d = [999999] * 10001
for _ in range(n):
    ary.append(int(sys.stdin.readline().rstrip()))
for i in range(n):
    d[ary[i]] = 1
min_ = min(ary)
for i in range(min_+1, 10001):
    for j in range(n):
        d[i] = min(d[i], d[i-ary[j]] + d[ary[j]])
if d[m] == 999999:
    print(-1)
else:
    print(d[m])