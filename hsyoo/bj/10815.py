import sys

def binary_search(ary, target, start, end):

    while start <= end:
        mid = (start + end) // 2
        if ary[mid] == target:
            return 1
        elif ary[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

n = int(input())
ary = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(input())
targets = list(map(int, sys.stdin.readline().rstrip().split()))
ary.sort()

for target in targets:
    print(binary_search(ary, target, 0, n-1), end = ' ')