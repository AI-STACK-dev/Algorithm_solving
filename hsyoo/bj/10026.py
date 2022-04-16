import copy
from collections import deque

n = int(input())
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
encode_x = {'R' : 1, 'G' : 2, 'B' : 3}
encode_o = {'R' : 1, 'G' : 1, 'B' : 2}

graph_x = [] 
graph_o = []
for _ in range(n):
    list_temp_x = []
    list_temp_o = []
    temp = list(input())
    for i in range(n):
        list_temp_x.append(encode_x[temp[i]])
        list_temp_o.append(encode_o[temp[i]])

    graph_x.append(list_temp_x)
    graph_o.append(list_temp_o)

def bfs(graph, coord, value, mode):
    if mode == 1:
        q = deque()
        q.append(coord)
        while q:
            y,x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx <0 or ny >= n or nx >= n:
                    continue
                if 1<=graph[ny][nx] <=3:
                    graph[ny][nx] = value
                    q.append((ny,nx))
    else:
        q = deque()
        q.append(coord)
        while q:
            y,x = q.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if ny < 0 or nx <0 or ny >= n or nx >= n:
                    continue
                if 1<=graph[ny][nx] <=2:
                    graph[ny][nx] = value
                    q.append((ny,nx))

# x먼저, o 다음
for k in range(1,3):
    if k == 1:
        graph = graph_x
        value = 4
    else:
        graph = graph_o
        value = 3
    for i in range(n):
        for j in range(n):
            if k == 1:
                if 1<=graph[i][j]<=3:
                    bfs(graph, (i,j), value, k)
                    value+=1
            elif k == 2:
                if 1<=graph[i][j]<=2:
                    bfs(graph, (i,j), value, k)
                    value+=1
    print(value-(4-k), end = ' ')
print()
