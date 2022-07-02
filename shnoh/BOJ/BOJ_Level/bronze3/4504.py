import sys; input = sys.stdin.readline;
n = int(input())
while True:
    x = int(input())
    if not x:
        break
    if x % n == 0:
        print(f'{x} is a multiple of {n}.')
    else:
        print(f'{x} is NOT a multiple of {n}.')