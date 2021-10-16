from collections import deque
def bfs(graph, v, visited):
    visited[v] = True
    queue = deque([v])
    while queue:
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
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