from sys import stdin
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end)//2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)
n = int(stdin.readline().rstrip())
ary = list(map(int, stdin.readline().rstrip().split()))
ary.sort()
m = int(stdin.readline().rstrip())
targets = list(map(int, stdin.readline().rstrip().split()))

for target in targets:
    result = binary_search(ary, target, 0, n-1)
    if result is not None:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')