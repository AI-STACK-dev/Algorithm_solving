import sys
k, n = map(int, input().split())
ary = []
for _ in range(k):
    ary.append(int(sys.stdin.readline().rstrip()))
ary.sort()
start = 1
end = ary[-1]

while start <= end:
    mid = (start + end) // 2
    value = 0
    for case in ary:
        value += (case // mid)
    if value >= n:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
print(result)