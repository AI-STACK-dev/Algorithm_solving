import sys; input=sys.stdin.readline
from collections import deque

m,n,h = map(int,input().split())
data = [ [ list(map(int,input().rstrip().split())) for _ in range(n)] for _ in range(h)]


d = deque([])
# 익지 않은 토마토 개수, 익은 토마토 좌표 append
cnt = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if data[i][j][k] == 0:
                cnt += 1
            elif data[i][j][k] == 1:
                d.append((i,j,k))

dh = [1,-1,0,0,0,0]
dn = [0,0,1,-1,0,0]
dm = [0,0,0,0,1,-1]

def bfs():
    global m,n,h,cnt
    day = 1
    while d:
        i,j,k = d.popleft()
        for idx in range(6):
            ii,jj,kk = i+dh[idx],j+dn[idx],k+dm[idx]
            if 0<=ii<h and 0<=jj<n and 0<=kk<m and data[ii][jj][kk] ==0:
                d.append((ii,jj,kk)) 
                data[ii][jj][kk] = data[i][j][k] +1
                day = max(day,data[ii][jj][kk])
                cnt -= 1      
    return day
day = bfs()
if cnt == 0:
    print(day-1)
else:
    print(-1)