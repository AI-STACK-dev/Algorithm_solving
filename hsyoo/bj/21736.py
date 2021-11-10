from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(graph, y,x):
    queue = deque([(y,x)])
    cnt = 0
    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0] + dy[i]
            nx = v[1] + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if graph[ny][nx] == 0:
                continue
            elif graph[ny][nx] == 1:
                queue.append((ny,nx))
                graph[ny][nx] += 1
            elif graph[ny][nx] == 3:
                cnt += 1
                queue.append((ny,nx))
                graph[ny][nx] = 2
    return cnt
n,m = map(int, input().split())
ary = []
for _ in range(n):
    ary.append(list(input()))

graph = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if ary[i][j] == 'O':
            graph[i][j] = 1
        elif ary[i][j] == 'P':
            graph[i][j] = 3
        elif ary[i][j] == 'I':
            graph[i][j] = 1
            y,x = i,j

value = bfs(graph, y, x)
if value == 0:
    print('TT')
else:
    print(value)
