import sys; input = sys.stdin.readline;
data = [input().rstrip() for _ in range(5)]
res = []
for i in range(5):
    n = len(data[i])
    for j in range(n - 3, -1, -1):
        if data[i][j:j+3] == 'FBI':
            res.append(i + 1)
res = list(set(res))
res.sort()
if res:
    print(*res, sep = ' ')
else:
    print("HE GOT AWAY!")