import sys; input = sys.stdin.readline;
while True:
    data = list(map(int, input().split()))
    if len(data) == 1:
        break
    a = data[0]
    cur = 1
    for i in range(a):
        cur = cur * data[2 * i + 1] - data[2 * i + 2]
    print(cur)