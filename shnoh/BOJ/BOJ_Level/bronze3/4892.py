import sys; input = sys.stdin.readline;
i = 0
while True:
    n0 = int(input())
    i += 1
    if not n0:
        break
    if n0 % 2:
        print(f'{i}. odd {(n0 - 1) // 2}')
    else:
        print(f'{i}. even {n0// 2}')