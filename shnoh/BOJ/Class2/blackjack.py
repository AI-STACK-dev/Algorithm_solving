import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
# 100 C 3? ok
comb = list(combinations(A, 3))
Max = 0
for a,b,c in comb:
    Sum = a + b + c
    if Sum <= m:
        Max = max(Max, Sum)
print(Max)

