import sys;input=sys.stdin.readline
from collections import deque

tc=int(input())

dx = [-2,-2,-1,-1,1,1,2,2]
dy = [1,-1,2,-2,2,-2,1,-1]

def dfs(n,a,b,c,d):
    visited = [[0]*n for _ in range(n)]
    q = deque([(a,b,0)])
    visited[a][b] = 1
    while q:
        a,b,count = q.popleft()

        if a == c and b == d:
            return count

        for i in range(8):
            x,y = a+dx[i],b+dy[i]
            if 0<= x<n and 0<=y<n:
                if visited[x][y] == 0:
                    q.append((x,y,count+1))
                    visited[x][y] = 1

for _ in range(tc):
    n = int(input())
    a,b = map(int,input().split())
    c,d = map(int,input().split())
    print(dfs(n,a,b,c,d))
