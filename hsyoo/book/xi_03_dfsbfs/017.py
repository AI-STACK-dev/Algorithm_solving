from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, k = map(int, input().split())
virus = []
graph = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(n):
        if temp[j] != 0:
            virus.append((i,j,temp[j], 0))
    graph.append(temp)

s,ay,ax = map(int, input().split())
virus.sort(key = lambda x : x[2])
queue = deque(virus)
while queue:
    v = queue.popleft()
    if v[3] == s:
        break
    for i in range(4):
        ny = v[0] + dy[i]
        nx = v[1] + dx[i]
        if ny <= -1 or ny >= n or nx <= -1 or nx >= n:
            continue
        if graph[ny][nx] != 0:
            continue
        elif graph[ny][nx] == 0:
            graph[ny][nx] = v[2]
            queue.append((ny,nx,v[2], v[3]+1))
print(graph[ay-1][ax-1])
