import sys; input = sys.stdin.readline;
n = int(input())
s='*' * (2 * n - 1)
for i in range(n):
    print('{}{}'.format(' '* i,s))
    s = s[2:]