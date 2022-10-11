import sys; input = sys.stdin.readline;
n = int(input())
for i in range(n):
    print(f'Case {i + 1}:')
    m = int(input())
    data = [int(input()) for _ in range(m)]
    for l in data:
        if l != 6:
            print(l + 1)