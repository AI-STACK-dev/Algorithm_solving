import sys; input = sys.stdin.readline;
m, n = map(int, input().split())

data = set([i for i in range(2,n + 1)])
to = int(n ** 0.5)
for i in range(2, to + 1):
    if i in data:
        for j in range(2 * i, n + 1, i):
            data.discard(j)
res = []
for num in data:
    if num >= m:
        res.append(num)
res.sort()
for num in res:
    print(num)