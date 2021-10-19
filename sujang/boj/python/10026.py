from sys import stdin
from collections import deque

input = stdin.readline
n = int(input().rstrip())

data = [[j for j in input().rstrip()] for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(i,j):
    global n 
    d = deque([[i,j]])
    visited[i][j] = 1
    while d:
        x,y = d.popleft()
        orig = data[x][y]
        for a,b in zip(dx,dy):
            X,Y = x+a,y+b
            if 0<=X<n and 0<=Y<n:
                if data[X][Y] == orig and visited[X][Y]==0:
                    d.append([X,Y])
                    visited[X][Y] = 1

visited = [[0]*n for _ in range(n)]
RGB = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] ==0:
            RGB += 1
            bfs(i,j)

for i in range(n):
    for j in range(n):
        if data[i][j] == 'R':
            data[i][j] ='G'
visited = [[0]*n for _ in range(n)]
XB = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] ==0:
            XB += 1
            bfs(i,j)
print(RGB,XB)