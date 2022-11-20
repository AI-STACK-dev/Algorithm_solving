import sys; input = sys.stdin.readline;
while True:
    a, b, c, d = map(int, input().split())
    if not a and not b and not c and not d:
        break
    print(c - b, d - a)