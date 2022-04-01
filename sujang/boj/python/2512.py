import sys; input = sys.stdin.readline

n = int(input())
data = list(map(int,input().split()))
target = int(input())

s,e = 0, max(data)
while s <= e:
    mid = (s+e)//2
    temp = 0
    for d in data:
        temp +=  mid if mid < d else d

    if temp <= target:
        s =  mid + 1
    elif temp > target:
        e = mid - 1
print(e)
