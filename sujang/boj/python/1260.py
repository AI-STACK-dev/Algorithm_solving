from sys import stdin
from collections import deque

# 입력
n,m,v = map(int,stdin.readline().rstrip().split())
data = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,stdin.readline().rstrip().split())
    data[a].append(b)
    data[b].append(a)
for i in range(n+1):
    data[i].sort()



visited = [0]*(n+1)
ans = []
def dfs(a):
    visited[a] = 1
    ans.append(a)
    for y in data[a]:
        if not visited[y]:
            dfs(y)
dfs(v)
print(*ans)

def bfs(a):
    global n
    visited = [0]*(n+1)
    d = deque([a])
    visited[a] = 1
    ans = [a]
    while d:
        x = d.popleft()
        for y in data[x]:
            if not visited[y]:
                visited[y]=1
                d.append(y)
                ans.append(y)
    return ans
print(*bfs(v))




