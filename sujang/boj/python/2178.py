import sys; input = sys.stdin.readline
from collections import deque

n,m = map(int,input().split())
data =  [ list(map(int,list(input().rstrip()))) for _ in range(n)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs():
    global n,m
    q = deque([[0,0]])
    while q:
        x,y = q.popleft()
        for i in range(4):
            a,b = x+dx[i],y+dy[i]
            if 0<=a<m and 0<=b<n and data[b][a] == 1:
                q.append([a,b])
                data[b][a] += data[y][x]
bfs()
print(data[n-1][m-1])
