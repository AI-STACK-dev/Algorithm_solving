import sys; input = sys.stdin.readline;
n, c = map(int, input().split())
data = [input().rstrip().split() for _ in range(n)]
res1 = 0
res2 = 0
k = 0
for i in range(n):
    res1 += int(data[i][0])
    if data[i][1][1] == 'e':
        res2 += int(data[i][0])
    if data[i][1][2] == 'l':
        k += int(data[i][0]) / 2
print(res1)
print(res2)
print(c * (res1 - k))