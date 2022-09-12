import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    n = int(input())
    print(f'Pairs for {n}: ', end = '')
    cnt = 0
    for i in range(1, (n + 1) // 2 ):
        if not cnt:
            print(f'{i} {n - i}', end = '')
        else:
            print(f', {i} {n - i}', end = '')
        cnt += 1
    print()