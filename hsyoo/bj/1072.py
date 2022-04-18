x,y = map(int, input().split())
z = y * 100 // x
start = 0
end = x
if z >= 99:
    print(-1)
else:
    cnt = 0
    while start <= end:
        cnt  += 1
        mid = (start + end) // 2
        temp = (y + mid) *100 // (x+mid)
        if temp != z:
            ans = mid
            end = mid -1
        else:
            start = mid + 1
    print(ans)