import sys; input = sys.stdin.readline;
n = int(input())
s='*' * (2 * n + 1)
for i in range(n):
    s = s[2:]
    print('{}{}'.format(' ' * i, s))
for i in range(n-2, -1, -1):
    s+='**'
    print('{}{}'.format(' ' * i, s))