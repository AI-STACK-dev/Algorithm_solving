
import sys
from sys import stdin

def count_by_value(array, target):
    n = len(array)
    a = first(array, target, 0, n-1)
    if a == None:
        return 0
    b = last(array, target, 0, n-1)
    return b-a+1

def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target and (mid == 0 or array[mid - 1] < target):
        return mid
    elif target <= array[mid]:
        return first(array, target, start, mid - 1)
    else:
        return first(array, target, mid + 1, end)
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target and (mid == n-1 or target < array[mid + 1]):
        return mid
    elif target < array[mid]:
        return last(array, target, start, mid - 1)
    else:
        return last(array, target, mid + 1, end)

n,x = map(int, stdin.readline().rstrip().split())
ary = list(map(int, stdin.readline().rstrip().split()))
count = count_by_value(ary, x)
if count == 0:
    print(-1)
else:
    print(count)


