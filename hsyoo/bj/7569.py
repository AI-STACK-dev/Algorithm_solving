from collections import deque
import sys

input = sys.stdin.readline
m,n,h = map(int, input().split())

starts = []
minus_list = []
graph =[]
for z in range(h):
    temp = []
    for y in range(n):
        a = list(map(int, input().split()))
        for x in range(m):
            if a[x] == 1:
                starts.append((z,y,x,0))
            if a[x] == -1:
                minus_list.append((z,y,x,0))
        temp.append(a)
    graph.append(temp)

dz = [1, -1, 0,0,0,0]
dy = [0,0,-1,0,1,0]
dx = [0,0,0,1,0,-1]

if len(minus_list) + len(starts) == (h * n * m):
    print(0)
else:
    q = deque(starts)
    while q:
        z,y,x,value = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nz < 0 or ny <0 or nx<0 or nz >= h or ny >=n or nx>=m:
                continue
            if graph[nz][ny][nx] == -1 or graph[nz][ny][nx] >= 1:
                continue
            if graph[nz][ny][nx] == 0:
                q.append((nz,ny,nx,value+1))
                graph[nz][ny][nx] = 1

    flag = 0
    for z in range(h):
        for y in range(n):
            for x in range(m):
                if graph[z][y][x] == 0:
                    flag = 1
                    break
            if flag == 1:
                break
        if flag == 1:
            break
    if flag == 1:
        print(-1)
    else:
        print(value)



