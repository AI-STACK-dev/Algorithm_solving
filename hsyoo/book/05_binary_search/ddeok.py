import sys
n,m = map(int, sys.stdin.readline().rstrip().split())
ary = list(map(int, sys.stdin.readline().rstrip().split()))

start = 0
end = max(ary)
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in ary:
        if x > mid:
            total += x - mid
    if total < m :
        end = mid - 1
    else:
        result = mid
        start = mid +1
print(result)