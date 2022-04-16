n = int(input())
ary = list(map(int, input().split()))
left = 0
right = n-1
ary.sort()
ans = ary[right] - ary[left]
al = left
ar = right
while right > left:
    temp = ary[right] + ary[left]
    if abs(temp) < abs(ans):
        ans = temp
        ar = right
        al = left
        if ans == 0:
            break
        
    if temp < 0:
        left += 1
    elif temp >= 0:
        right -= 1

print(ary[al], ary[ar])