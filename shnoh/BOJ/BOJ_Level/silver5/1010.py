import sys; input = sys.stdin.readline;
import math
t = int(input())
# mCn-m
for _ in range(t):
    n, m = map(int, input().split())
    res = math.factorial(m) // math.factorial(m - n) // math.factorial(n)
    print(res)