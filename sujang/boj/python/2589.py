from sys import stdin
from collections import deque
import copy

n,m = list(map(int,stdin.readline().rstrip().split()))
data = [[ 1 if a =='L' else 0 for a in stdin.readline().rstrip()] for _ in range(n)]
# print(*data,sep='\n')
visited = [[0]*m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y):
    v = copy.deepcopy(visited)
    v[x][y] = 1
    d = deque([[x,y]])
    cnt = 0
    while d:
        x,y = d.popleft()
        for ax,ay in zip(dx,dy):
            X,Y = x+ax,y+ay
            if 0<=X<n and 0<=Y<m:
                if data[X][Y] == 1 and v[X][Y] ==0:
                    v[X][Y] = v[x][y]+1
                    cnt = max(cnt,v[X][Y]-1)
                    d.append([X,Y])
    return cnt
ans = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 1:
            ans = max(ans,bfs(i,j))
print(ans)