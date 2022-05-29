import sys; input = sys.stdin.readline;
n = int(input())
s='*'
for i in range(n):
    print('{}{}'.format(' '*(n-i-1),s))
    s+='**'
s='*' * (2 * n - 3)
for i in range(1,n):
    print('{}{}'.format(' '* i,s))
    s = s[2:]