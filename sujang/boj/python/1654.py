import sys;input=sys.stdin.readline
k,n = map(int,input().split())
data = [int(input()) for _ in range(k)]
start,end = 1,max(data)
while start <= end:
    mid = (start+end)//2
    num = 0 
    for d in data:
        num += d // mid
    if num >= n:
        start = mid + 1
    else:
        end = mid-1
print(end)