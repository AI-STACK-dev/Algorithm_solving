import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    d = int(input())
    for i in range(1, 100):
        if d < i + i ** 2:
            print(i - 1)
            break