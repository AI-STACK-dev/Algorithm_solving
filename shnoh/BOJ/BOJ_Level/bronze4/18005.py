import sys; input = sys.stdin.readline;
n = int(input())
if n % 4 == 0:
    print(2)
elif n % 2 == 0:
    print(1)
else:
    print(0)