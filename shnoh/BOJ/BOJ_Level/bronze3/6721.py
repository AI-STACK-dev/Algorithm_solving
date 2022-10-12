import sys; input = sys.stdin.readline;
def reverse(s):
    res = []
    for c in s:
        res.insert(0, c)
    return ''.join(res)
n = int(input())
for _ in range(n):
    a, b = input().rstrip().split()
    a = int(reverse(a))
    b = int(reverse(b))
    Sum = int(reverse(str(a + b)))
    print(Sum)