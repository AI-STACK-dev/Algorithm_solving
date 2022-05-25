import sys; input = sys.stdin.readline;
n = int(input())
s='*'
for i in range(n):
    print('{}{}'.format(' '*(n-i-1),s))
    s+='**'