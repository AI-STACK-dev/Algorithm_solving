import sys; input = sys.stdin.readline;
n, t, c, p = map(int, input().split())
res = ((n - 1) // t) * c  * p
print(res)