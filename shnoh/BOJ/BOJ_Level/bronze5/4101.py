import sys; input = sys.stdin.readline;
while True:
    a, b = map(int, input().split())
    if not a:
        break
    if a > b:
        print("Yes")
    else:
        print("No")