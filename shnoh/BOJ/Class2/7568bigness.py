import sys; input = sys.stdin.readline;
n = int(input())
data = []
for _ in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(n):
    cnt = 1
    for x, y in data:
        if data[i][0] < x and data[i][1] < y:
            cnt += 1
    print(cnt)