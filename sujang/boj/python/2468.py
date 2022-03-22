import sys; input = sys.stdin.readline
from collections import deque

n = int(input())
field = [list(map(int,input().split())) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(a,b,level):
    q = deque([(a,b)])
    visited[a][b] = 1
    while q:
        a,b = q.popleft()
        for i in range(4):
            x,y = a+dx[i],b+dy[i]
            if 0<=x<n and 0<=y<n:
                if field[x][y] > level and visited[x][y] == 0:
                    q.append((x,y))
                    visited[x][y] = 1

ans = 1
for level in range(1,101):
    visited =[[0]*n for _ in range(n)]
    temp = 0
    for i in range(n):
        for j in range(n):
            if field[i][j] > level and visited[i][j]==0:
                dfs(i,j,level)
                temp += 1
    ans = max(temp,ans)
print(ans)    
