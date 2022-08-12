import sys; input = sys.stdin.readline;
while True:
    c = float(input())
    if not c:
        break
    res = 0
    i = 0
    while res < c:
        i += 1
        res += 1 / (i + 1)
    print(f'{i} card(s)')