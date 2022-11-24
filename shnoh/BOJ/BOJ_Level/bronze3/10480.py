import sys; input = sys.stdin.readline;
t = int(input())
for i in range(t):
    x = int(input())
    if x % 2:
        print(f"{x} is odd")
    else:
        print(f"{x} is even")