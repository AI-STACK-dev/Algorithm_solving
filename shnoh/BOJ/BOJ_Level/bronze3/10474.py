import sys; input = sys.stdin.readline;
while True:
    a, b = map(int, input().split())
    if b == 0:
        break
    print(f"{a // b} {a % b} / {b}")