import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    n = int(input())
    res = 0
    for j in range(n):
        data = list(input().rstrip().split())
        for k in range(2):
            if data[k] == 'R':
                data[k] = 1
            elif data[k] == 'S':
                data[k] = 2
            else:
                data[k] = 3
        if data[0] + 1 == data[1] or data[0] - 2 == data[1]:
            res += 1
        elif data[1] + 1 == data[0] or data[1] - 2 == data[0]:
            res -= 1
    if res > 0:
        print("Player 1")
    elif res < 0:
        print("Player 2")
    else:
        print("TIE")