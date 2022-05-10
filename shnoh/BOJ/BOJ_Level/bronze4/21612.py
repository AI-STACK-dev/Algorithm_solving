import sys; input = sys.stdin.readline;
b = int(input())
p = 5 * b - 400
print(p)
if b > 100:
    print(-1)
elif b == 100:
    print(0)
else:
    print(1)