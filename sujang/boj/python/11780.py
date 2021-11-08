from sys import stdin
import sys
INF = sys.maxsize

n = int(stdin.readline().rstrip())
m = int(stdin.readline().rstrip())
distance = [ [INF]*n for _ in range(n) ]
track = [ [None]*n for _ in range(n) ]

for i in range(n):
    distance[i][i] = 0
    
for _ in range(m):
    a,b,c = map(int,stdin.readline().rstrip().split())
    distance[a-1][b-1] = min(c,distance[a-1][b-1])

for a in range(n):
    for b in range(n):
        for c in range(n):
            if distance[b][c] > distance[b][a]+distance[a][c]:
                distance[b][c] = distance[b][a]+distance[a][c]
                track[b][c] = a

for i in range(n):
    for j in range(n):
        if distance[i][j] == INF:
            distance[i][j] = 0

for i in range(n):
    print(*distance[i]) 

def rtnpath(a,b):
    if track[a][b] == None:
        return []
    else:
        v = track[a][b]
        return rtnpath(a,v) + [v] + rtnpath(v,b)


for a in range(n):
    for b in range(n):
        if a==b or distance[a][b] == 0:
            print(0)
        else:
            path = [a] + rtnpath(a,b) + [b]
            path = [ p+1 for p in path]
            print(len(path),end=' ')
            print(*path)

