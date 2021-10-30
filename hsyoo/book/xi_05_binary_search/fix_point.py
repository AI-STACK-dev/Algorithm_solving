import sys

def binary_search(ary, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if ary[mid] == mid:
        return mid
    elif ary[mid] > mid:
        return binary_search(ary, start, mid - 1)
    else:
        return binary_search(ary, mid + 1, end)

n = int(input())
ary = list(map(int, sys.stdin.readline().rstrip().split()))

value = binary_search(ary, 0, n-1)
if value == None:
    print(-1)
else:
    print(value)