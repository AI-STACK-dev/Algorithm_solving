import sys;input = sys.stdin.readline
from collections import deque

n = int(input())
m = int(input())
data =[ [] for _ in range(n+1)]
visited = [False]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    data[a].append(b)
    data[b].append(a)

q = deque([1])
visited[1] = True
ans = 0
while q:
    x = q.popleft()
    for d in data[x]:
        if not visited[d]:
            ans += 1
            q.append(d)
            visited[d]=True
print(ans)