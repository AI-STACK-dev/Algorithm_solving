import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(array)

while start <= end:
    mid = (start + end) // 2
    total = 0
    for x in array:
        if x > mid:
            total += (x-mid)
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)