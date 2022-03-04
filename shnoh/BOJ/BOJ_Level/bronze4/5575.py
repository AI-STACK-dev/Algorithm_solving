import sys; input = sys.stdin.readline;
for _ in range(3):
    data = list(map(int, input().split()))
    if data[5] < data[2]:
        data[4] -= 1
        data[5] += 60
    if data[4] < data[1]:
        data[3] -= 1
        data[4] += 60
    print(data[3] - data[0], data[4] - data[1], data[5] - data[2])