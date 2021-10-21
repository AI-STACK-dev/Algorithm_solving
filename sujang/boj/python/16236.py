from sys import stdin
from collections import deque

input = stdin.readline
n = int(input().rstrip())
field = []
for i in range(n):
    field.append(list(map(int,input().rstrip().split())))
    for j in range(n):
        if field[i][j]==9:
            baby_shark = [i,j]
            field[i][j] = 0


dx = [0,0,1,-1]
dy = [1,-1,0,0]
ans = 0
def bfs(I,J,SIZE,TIME):
    global n
    eat =[]
    d = deque([[I,J,TIME]])
    while d:
        i,j,time= d.popleft()
        for idx in range(4):
            X,Y = i+dx[idx],j+dy[idx]
            if 0<=X<n and 0<=Y<n and visited[X][Y]==0:
                if field[X][Y] < SIZE and field[X][Y] !=0:
                    eat.append([X,Y,time+1])
                elif field[X][Y] <= SIZE or field[X][Y] ==0:
                    visited[X][Y]=1
                    d.append([X,Y,time+1])
    if not eat:
        return -1,-1,TIME
    else:
        eat.sort(key=lambda x: (x[2],x[0],x[1]))
        return eat[0]
    
                

I,J = baby_shark[0],baby_shark[1]
time = exp = 0
size = 2
while True:
    visited = [[0]*n for _ in range(n)]
    visited[I][J] = 1
    I,J,time = bfs(I,J,size,time)
    if I==-1:
        break
    field[I][J] = 0
    exp+=1
    if exp==size:
        exp=0
        size +=1

print(time)