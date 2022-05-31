import sys; input = sys.stdin.readline;
def Sum(a,b):
    return b * (b + 1) // 2 - a * (a + 1) // 2
a, b = map(int, input().split())
a, b = min(a,b), max(a,b)
if a * b <= 0:
    a = abs(a)
    if abs(a) < abs(b):
        res = Sum(a, b)
    else:
        res = - Sum(b, a)
else:
    res = Sum(a - 1, b)
print(res)