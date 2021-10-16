from itertools import  combinations
from collections import deque
from sys import stdin
import copy as cp

ans = 0
dx = [1,0,0,-1]
dy = [0,1,-1,0]
n,m = list(map(int, stdin.readline().split()))
data = [list(map(int, stdin.readline().split())) for _ in range(n)]

zeros = []
twos = []
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            zeros.append([i,j])
        if data[i][j] == 2:
            twos.append([i,j])

def bfs(cc):
    global ans
    cnt = 0
    ## 3개의 벽 만들기
    temp = cp.deepcopy(data)
    for a,b in cc:
        temp[a][b] = 1
    
    ## 
    d = deque([])
    for t in twos:
        d.append(t)
    
    while d:
        x,y = d.popleft()
        for da,db in zip(dx,dy):
            X,Y = x+da,y+db
            if X>=0 and Y>=0 and X < n and Y < m:
                if temp[X][Y] ==0:
                    d.append([X,Y])
                    temp[X][Y] = 2

    for i in range(n):
        cnt += temp[i].count(0)
    if ans < cnt:
        ans = cnt


all_cases = list(combinations(zeros,3))
for cc in all_cases:
    bfs(cc)

print(ans)
    
    