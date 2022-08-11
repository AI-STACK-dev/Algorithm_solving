import sys; input = sys.stdin.readline;
while True:
    n = int(input())
    if n == -1:
        break;
    data = [list(map(int, input().split())) for _ in range(n)]
    res = data[0][0] * data[0][1]
    for i in range(1, n):
        res += (data[i][1] - data[i - 1][1]) * data[i][0]
    print(f'{res} miles')