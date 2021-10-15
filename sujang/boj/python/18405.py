from sys import stdin
from collections import deque

n,k = list(map(int,stdin.readline().rstrip().split()))
tube = []
data = []
for i in range(n):
    tube.append(list(map(int,stdin.readline().rstrip().split())))
    for j in range(n):
        if tube[i][j] !=0:
            data.append([tube[i][j],0,i,j])
s,tx,ty = list(map(int,stdin.readline().rstrip().split()))
dx = [0,0,1,-1]
dy = [1,-1,0,0]
if s != 0:
    data.sort()
    deq=deque(data)
    while deq:
        v,S,x,y = deq.popleft()
        if S==s:
            break
        for da,db in zip(dx,dy):
            X,Y= x+da,y+db
            if 0<=X<n and 0<=Y<n:
                if tube[X][Y]==0:
                    tube[X][Y]=v
                    deq.append([v,S+1,X,Y])
print(tube[tx-1][ty-1])
                    