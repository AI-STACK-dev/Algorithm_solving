from bisect import bisect_left, bisect_right
from sys import stdin

def check_cnt(ary, target):
    first = bisect_left(ary, target)
    last = bisect_right(ary, target)
    return (last - first)

n = int(input())
ary = list(map(int, stdin.readline().rstrip().split()))
m = int(input())
targets = list(map(int, stdin.readline().rstrip().split()))
ary.sort()

for target in targets:
    print(check_cnt(ary, target), end = ' ')