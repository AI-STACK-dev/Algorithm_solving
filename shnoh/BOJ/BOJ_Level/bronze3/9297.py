import sys; input = sys.stdin.readline;
t = int(input())
for i in range(1, t + 1):
    n, d =  map(int, input().split())
    I = n // d
    r = n % d
    if r == 0:
        print(f'Case {i}: {I}')
    elif I == 0:
        print(f'Case {i}: {r}/{d}')
    else:
        print(f'Case {i}: {I} {r}/{d}')