from collections import deque

n = int(input())
m = int(input())

graph  = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False] * (n+1)


def bfs(graph, start, visited):
    visited[start] = True
    q = deque()
    q.append(start)

    while q:
        now = q.popleft()
        for i in graph[now]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True
bfs(graph, 1, visited)
print(sum(visited)-1)
