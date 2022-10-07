import sys; input = sys.stdin.readline;
n = int(input())
s='*' * n
for i in range(n):
    print('{}{}'.format(' ' * (n - i - 1), '*' * (i + 1)))
for i in range(n-2, -1, -1):
    print('{}{}'.format(' ' * (n - i - 1), '*' * (i + 1)))