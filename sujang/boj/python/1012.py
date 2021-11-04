from sys import stdin
from collections import deque

t = int(stdin.readline().rstrip())

dx = [1,-1,0,0] 
dy = [0,0,1,-1]

def bfs(field,visited,x,y,m,n):
    d = deque([[x,y]])
    visited[y][x] = 1
    while d:
        x,y = d.popleft()
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<m and 0<=b<n:
                if field[b][a]==1 and  visited[b][a] == 0:
                    visited[b][a] = 1
                    d.append([a,b])
    return visited

ans =[]
for _ in range(t):
    m,n,k = map(int,stdin.readline().rstrip().split())
    field = [[0]*m for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    for _ in range(k):
        x,y = map(int,stdin.readline().rstrip().split())
        field[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if field[i][j]==1 and  visited[i][j]==0:
                visited = bfs(field,visited,j,i,m,n)
                cnt +=1
    ans.append(cnt)

print(*ans,sep='\n')

    