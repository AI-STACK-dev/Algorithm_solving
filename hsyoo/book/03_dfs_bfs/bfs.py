from collections import deque

def bfs(graph, start, visited):
    q = deque()
    visited[start] = True
    q.append(start)
    while q:
        now = q.popleft()
        print(now, end = ' ')
        for i in graph[now]:
            if visited[i] == False:
                q.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
visited = [False] * len(graph)

bfs(graph, 1, visited)
print()

