import sys; input = sys.stdin.readline
from collections import deque

dx = [0,0,1,-1,1,1,-1,-1]
dy = [1,-1,0,0,1,-1,-1,1]

def dfs(i, j):
    q = deque([(i,j)])
    visited[i][j] = 1
    while q:
        a,b = q.popleft()
        for k in range(8):
            x,y = a+dx[k],b+dy[k]
            if 0<=x<h and 0<=y<w: 
                if field[x][y] == 1 and visited[x][y] == 0:
                    q.append((x,y))
                    visited[x][y] = 1


while True:
    w,h = map(int,input().split())
    if w ==0 and h ==0 :
        break
    field = [list(map(int,input().split())) for _ in range(h)]
    visited = [ [0]*w for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if field[i][j] == 1 and visited[i][j] == 0:
                dfs(i, j)
                cnt += 1
    print(cnt)
