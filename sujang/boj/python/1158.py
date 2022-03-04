from collections import deque

n,m = map(int,input().split())
data = deque(list(range(1,n+1)))
ans = []
count = 1
while data:
    if count == m:
        count = 1
        ans.append(data.popleft())
    else:
        count += 1
        data.append(data.popleft()) 

print("<",end='');print(*ans,sep=", ",end=">\n")
