import sys; input = sys.stdin.readline;
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    c = a - b
    d = c % 2
    e = c // 2
    if d:
        e -= 1
    if e < 0:
        e = 0
        d = 0
    print(e, d)