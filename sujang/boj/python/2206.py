import sys;input=sys.stdin.readline
from collections import deque as dq

n,m = map(int,input().split())
graph = [list(map(int,list(input().rstrip()))) for _ in range(n)]
visited = [[ [0]*2 for __ in range(m)] for _ in range(n)]

def bfs(i,j,isC):
    q = dq([[i,j,isC]])
    visited[i][j][isC] = 1
    while q:
        a,b,c = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for i in range(4):
            x,y = a+dx[i] , b+dy[i]
            if 0<=x<n and 0<=y<m:
                if graph[x][y] == 0 and  visited[x][y][c] == 0:
                    q.append([x,y,c])
                    visited[x][y][c] = visited[a][b][c] + 1
                if graph[x][y] == 1 and c == 0:
                    q.append([x,y,c+1])
                    visited[x][y][c+1] = visited[a][b][c]+1
    return -1
dx = [1,0,0,-1]
dy = [0,1,-1,0]
print(bfs(0,0,0))
