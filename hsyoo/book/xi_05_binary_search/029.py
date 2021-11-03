n, c = map(int, input().split())
ary = []
for _ in range(n):
    ary.append(int(input()))
ary.sort()

start = ary[1] - ary[0]
end = ary[-1] - ary[0]

while (start <= end):
    mid = (start + end) // 2
    value = ary[0]
    count = 1
    for i in range(1,n):
        if ary[i] >= value + mid:
            value = ary[i]
            count += 1
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)