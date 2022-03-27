import sys; input = sys.stdin.readline;
b1, b2, b3 = map(int, input().split())
c1, c2, c3 = map(int, input().split())
x = z = c1 - b1
y = z + 1
if 100 * b2 + b3 > 100 * c2 + c3:
    x -= 1
print(x)
print(y)
print(z)