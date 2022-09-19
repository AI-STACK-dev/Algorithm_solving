import sys; input = sys.stdin.readline;
while True:
    data = list(map(int, input().split()))
    cnt = 0
    if not data[0]:
        break
    while len(set(data)) != 1:
        temp = [abs(data[0] - data[1]), abs(data[1] - data[2]), abs(data[2] - data[3]), abs(data[3] - data[0])]
        data = temp
        cnt += 1
    print(cnt)