from bisect import bisect_right,bisect_left
n = int(input())
data = list(map(int,input().split()))
m = int(input())
test = list(map(int,input().split()))
data.sort()
for i in test:
    left = bisect_left(data,i)
    right = bisect_right(data,i)
    if left == right:
        print(0)
    else:
        print(1)