from collections import deque
dy = [-1,0,1,0]
dx = [0,1,0,-1]
t = int(input())


def bfs(graph, coord, value):
    q = deque()
    q.append(coord)
    graph[coord[0]][coord[1]] = value
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx <0 or ny >= n or nx >= m:
                continue
            if graph[ny][nx] == 1:
                q.append((ny,nx))
                graph[ny][nx] = value
    
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    
    value = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                value += 1
                bfs(graph, (i,j), value)
    print(value-1)
    

