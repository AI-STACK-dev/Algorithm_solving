from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, list(input()))))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

q = deque()
# (ny, nx, cnt)
q.append((0,0,1))
graph[0][0] = 2
while q:
    y, x, cnt = q.popleft()
    if y == n-1 and x == m-1:
        print(cnt)
        break
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if graph[ny][nx] == 1:
            q.append((ny,nx,cnt+1))
            graph[ny][nx] = 2


