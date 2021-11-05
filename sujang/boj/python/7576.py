from sys import stdin
from collections import deque

m,n = map(int,stdin.readline().rstrip().split())
data = [ list(map(int,stdin.readline().rstrip().split())) for _ in range(n) ]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

visited = [[0]*m for _ in range(n)]
d = deque([])
cnt = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            d.append([i,j,0,cnt])
            cnt+=1

def bfs():
    global n,m,cnt
    ans = [0] * cnt
    while d:
        x,y,day,num = d.popleft()
        for i in range(4):
            a,b = x+dx[i] , y+dy[i]
            if 0<=a<n and 0<=b<m:
                if data[a][b] ==0 and visited[a][b] ==0:
                    visited[a][b] = 1
                    data[a][b] = 1
                    ans[num] = day+1
                    d.append([a,b,day+1,num])
    return ans

ans = bfs()

cnt = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 1 or data[i][j] == -1:
            cnt+=1
if cnt == m*n:
    print(max(ans))
else:
    print(-1)