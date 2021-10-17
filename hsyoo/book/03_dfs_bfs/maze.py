from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs(graph, y, x):
    queue = deque([(y,x)])
    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0] + dy[i]
            nx = v[1] + dx[i]
            # print(ny, nx)
            if ny <= -1 or nx <= -1 or ny >= n or nx >= m:
                continue
            if graph[ny][nx] == 0:
                continue
            elif graph[ny][nx] == 1:
                queue.append((ny,nx))
                graph[ny][nx] = graph[v[0]][v[1]] + 1
    return graph[n-1][m-1]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
print(bfs(graph, 0, 0))
