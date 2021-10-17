from collections import deque
import copy

def bfs(graph, start_coords, empty_coords, zero_coords):
    if len(zero_coords) == 0:
        return 0
    queue = deque(start_coords)
    pre = copy.deepcopy(start_coords)
    cnt = 1
    while queue:        
        sum_ = 0
        y,x = queue.popleft()
        flag = 1
        if (y,x) in pre:
            flag = 0
        if flag == 1:
            cnt += 1
            pre = copy.deepcopy(list(queue))
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 1:
                    sum_ += 1
        if sum_ == n*m-len(empty_coords):            
            return cnt
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if ny <= -1 or nx <= -1 or ny >= n or nx >= m:
                continue
            if graph[ny][nx] == 0:
                queue.append((ny,nx))
                graph[ny][nx] = 1
    return -1
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

m,n = map(int, input().split())
graph = []
start_coords = []
empty_coords = []
zero_coords = []
for y in range(n):
    temp = list(map(int, input().split()))
    for x in range(m):
        if temp[x] == 1:
            start_coords.append((y,x))
        elif temp[x] == -1:
            empty_coords.append((y,x))
        else:
            zero_coords.append((y,x))
    graph.append(temp)

print(bfs(graph, start_coords, empty_coords, zero_coords))
