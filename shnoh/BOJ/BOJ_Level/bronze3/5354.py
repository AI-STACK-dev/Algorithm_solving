import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    n = int(input())
    updown = '#' * n
    print(updown)
    mid = '#' + 'J' * (n - 2) + '#'
    for j in range(n - 2):
        print(mid)
    if n != 1:
        print(updown)
    print()