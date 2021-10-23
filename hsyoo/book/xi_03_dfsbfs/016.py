from itertools import combinations
from collections import deque
import copy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs(graph, virus, wall):
    temp_graph = copy.deepcopy(graph)
    queue = deque(virus)
    for y,x in wall:
        temp_graph[y][x] = 1
    while queue:
        v = queue.popleft()
        for i in range(4):
            ny = v[0]+dy[i]
            nx = v[1]+dx[i]
            if ny <= -1 or ny >= n or nx <= -1 or nx >= m:
                continue
            if temp_graph[ny][nx] == 1 or temp_graph[ny][nx] == 2:
                continue
            elif temp_graph[ny][nx] == 0:
                temp_graph[ny][nx] = 2
                queue.append((ny,nx))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if temp_graph[i][j] == 0:
                cnt += 1
    return cnt

n, m = map(int, input().split())
graph = []
virus = []
zeros = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 2:
            virus.append((i,j))
        elif temp[j] == 0:
            zeros.append((i,j))
    graph.append(temp)

comb = list(combinations(zeros, 3))
result = []
for coord in comb:
    cnt = bfs(graph, virus, coord)
    result.append(cnt)

print(max(result))