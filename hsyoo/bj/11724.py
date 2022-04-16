from collections import deque

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(graph, start, visited, value):
    q = deque()
    q.append(start)
    visited[start] = value
    
    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] != 0:
                continue
            q.append(i)
            visited[i] = value

value = 1
# max_ = -1
for num in range(1,n+1):
    if visited[num] == 0:
        bfs(graph, num, visited, value)
        value += 1

print(max(visited))

