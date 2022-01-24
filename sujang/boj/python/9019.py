import sys;input = sys.stdin.readline
from collections import deque

def bfs(a,b):
    d = deque()
    d.append((a,""))
    visited = [0]*10000
    visited[a] = 1
    
    while d:
        num, string = d.popleft()
        if num == b:
            return string

        # D
        D = (num*2) % 10000
        if visited[D] == 0:
            d.append((D,string+"D"))
            visited[D] = 1
        
        # S
        S = num - 1 if num !=0 else 9999
        if visited[S] == 0: 
            d.append((S,string+"S"))
            visited[S] = 1
    
        # L
        L = int(((num%1000)*10) + num//1000)
        if visited[L] == 0: 
            d.append((L,string+"L"))
            visited[L] = 1    
        
        
        # R
        R = int(((num%10)*1000) + num//10)
        if visited[R] == 0:
            d.append((R,string+"R"))
            visited[R] = 1


tc = int(input().rstrip())
for _ in range(tc):
    a,b = map(int,input().rstrip().split())
    print(bfs(a,b))
