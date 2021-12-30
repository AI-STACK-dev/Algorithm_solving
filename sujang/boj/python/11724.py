from collections import deque
import sys; input = sys.stdin.readline

n,m = map(int,input().split())
graph = [ [] for _ in range(n+1)]
visited = [False]*(n+1)


for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited[start] = True
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)

ans = 0
for i in range(1,n+1):
    if visited[i] == False:
        bfs(i)
        ans +=1
print(ans)