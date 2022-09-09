import sys; input = sys.stdin.readline;
while True:
    N = int(input())
    if not N:
        break
    res = N ** 2 - N + 1
    print(f'{N} => {res}')