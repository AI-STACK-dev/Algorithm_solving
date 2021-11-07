import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))
S, X, Y = map(int, sys.stdin.readline().split())
B = []
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(n):
        if A[i][j] != 0:
            B.append([A[i][j], i, j, 0])
B.sort()
q = deque(B)
while q:
    vn, x, y, s = q.popleft()
    if s == S: break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        elif A[nx][ny] == 0:
            A[nx][ny] = vn
            q.append((vn, nx, ny, s + 1))
print(A[X-1][Y-1])