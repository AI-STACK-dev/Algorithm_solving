import sys; input = sys.stdin.readline
n = int(input())
data = list(map(int,input().split()))

fromLeft = [1]*n
for i in range(1,n):
    for j in range(i):
        if data[i] > data[j]:
            fromLeft[i] = max(fromLeft[i], fromLeft[j]+1)


fromright = [1]*n
for i in range(n-2,-1,-1):
    for j in range(n-1,i,-1):
        if data[i] > data[j]:
            fromright[i] = max(fromright[i], fromright[j]+1)

ans = 0
for i in range(n):
    ans = max(ans,fromLeft[i] + fromright[i] - 1)
print(ans)
