from bisect import bisect_left, bisect_right
import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
ary = list(map(int, sys.stdin.readline().rstrip().split()))
if x in set(ary):
    print(bisect_right(ary, x) - bisect_left(ary, x))
else:
    print(-1)