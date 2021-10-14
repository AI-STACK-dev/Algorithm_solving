from sys import stdin
from collections import deque


n,m,k,x = list(map(int,stdin.readline().rstrip().split()))
visited =[0]*(n+1)
graph = [[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = list(map(int,stdin.readline().rstrip().split()))
    graph[a].append(b)



def bfs(x):
    d = deque([x])
    visited[x]=1
    ans = []
    while d:
        p = d.popleft()
        for b in graph[p]:
            if visited[b] ==0:
                visited[b] = visited[p]+1
                d.append(b)
                if visited[b] == k+1:
                    ans.append(b)
    return ans

a=bfs(x)
if a==[]:
    print(-1)
else:
    a.sort()
    print(*a,sep='\n')

