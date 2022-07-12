n = int(input())
arr = list(map(int, input().split()))

start = 0
end = n - 1
flag = 0
while start <= end:
    mid = (start + end)
    if mid > arr[mid]:
        start = mid + 1
    elif mid < arr[mid]:
        end = mid - 1
    else:
        flag = 1
        break
if flag == 0:
    print(-1)
else:
    print(mid)