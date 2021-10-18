from sys import stdin
from collections import deque

n,l,r = map(int,stdin.readline().rstrip().split())
world = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(i,j):
    global n,l,r
    s=world[i][j]
    united = [[i,j]]
    d = deque([[i,j]])
    visited[i][j]=1
    while d:
        x,y = d.popleft()
        orig = world[x][y]
        for a,b in zip(dx,dy):
            X,Y = x+a,y+b
            if 0<=X<n and 0<=Y<n:
                if visited[X][Y]==0 and l<= abs(orig-world[X][Y])<=r:
                    visited[X][Y]=1
                    s += world[X][Y]
                    d.append([X,Y])
                    united.append([X,Y])
    if len(united) > 1:
        target = s//len(united)
        for x,y in united:
            world[x][y]=target
        return True
    else:
        return False
    

def check():
    rtn = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                if bfs(i,j):
                    rtn = True
    return rtn
day = 0
while check():
    day+=1
    visited = [[0]*n for _ in range(n)]

print(day)
