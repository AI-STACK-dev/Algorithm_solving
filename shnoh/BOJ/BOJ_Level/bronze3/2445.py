import sys; input = sys.stdin.readline;
n = int(input())
s='*'
for i in range(n):
    print('{}{}{}'.format(s, ' '*(2 * (n - i - 1)), s))
    s+='*'
s='*' * (n - 1)
for i in range(1,n):
    print('{}{}{}'.format(s, ' ' * (2 * i), s))
    s = s[1:]