import sys; input = sys.stdin.readline;
from collections import deque
t = int(input())
queue = deque()
for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        cabbage[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if cabbage[i][j] == 1:
                cabbage[i][j] = 0
                cnt += 1
                queue.append((i,j))
                while queue:
                    nx, ny = queue.popleft()
                    if nx + 1 < n and cabbage[nx + 1][ny] == 1 :
                        cabbage[nx + 1][ny] = 0
                        queue.append((nx + 1,ny))
                    if ny + 1 < m and cabbage[nx][ny + 1] == 1:
                        cabbage[nx][ny + 1] = 0
                        queue.append((nx,ny + 1))
                    if nx - 1 >= 0 and cabbage[nx - 1][ny] == 1:
                        cabbage[nx - 1][ny] = 0
                        queue.append((nx - 1,ny))
                    if ny - 1 >= 0 and cabbage[nx][ny - 1] == 1:
                        cabbage[nx][ny - 1] = 0
                        queue.append((nx,ny - 1))
    print(cnt)
# for _ in range(t):
#     m, n, k = map(int, input().split())
#     visited = [[False] * m for _ in range(n)]
#     cabbage = [[0] * m for _ in range(n)]
#     for _ in range(k):
#         x, y = map(int, input().split())
#         cabbage[y][x] = 1
#     cnt = 0
#     for i in range(n):
#         for j in range(m):
#             if not visited[i][j] and cabbage[i][j] == 1:
#                 visited[i][j] = True
#                 cnt += 1
#                 queue.append((i,j))
#                 while queue:
#                     nx, ny = queue.popleft()
#                     if nx + 1 < n and cabbage[nx + 1][ny] == 1 and not visited[nx + 1][ny]:
#                         visited[nx + 1][ny] = True
#                         queue.append((nx + 1,ny))
#                     elif ny + 1 < m and cabbage[nx][ny + 1] == 1 and not visited[nx][ny + 1]:
#                         visited[nx][ny + 1] = True
#                         queue.append((nx,ny + 1))
#                     elif nx - 1 >= 0 and cabbage[nx - 1][ny] == 1 and not visited[nx - 1][ny]:
#                         visited[nx - 1][ny] = True
#                         queue.append((nx - 1,ny))
#                     elif ny - 1 >= 0 and cabbage[nx][ny - 1] == 1 and not visited[nx][ny - 1]:
#                         visited[nx][ny - 1] = True
#                         queue.append((nx,ny - 1))
#             else:
#                 visited[i][j] = True
#     print(cnt)
