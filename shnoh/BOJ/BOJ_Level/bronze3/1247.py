import sys; input = sys.stdin.readline;
for i in range(3):
    N = int(input())
    data = [int(input()) for _ in range(N)]
    res = sum(data)
    if res > 0:
        print('+')
    elif res < 0:
        print('-')
    else:
        print(0)