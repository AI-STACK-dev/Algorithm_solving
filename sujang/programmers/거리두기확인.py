from collections import deque

def bfs(li,x,y,n):
    visited = [[0]*n for _ in range(n)]
    dx,dy = [1,-1,0,0], [0,0,1,-1]
    q = deque([(x,y,0)])
    visited[x][y] = 1
    while q:
        i,j,l = q.popleft()
        for k in range(4):
            x,y = i + dx[k], j + dy[k]
            if 0<=x<n and 0<=y<n and visited[x][y] == 0 and l+1 <= 2:
                if li[x][y] == "P":
                    return True
                elif li[x][y] == "O":
                    visited[x][y] = 1
                    q.append((x,y,l+1))
    return False
        
def isPossible(li):
    n = len(li)
    for i in range(n):
        for j in range(n):
            if li[i][j] == "P":
                if bfs(li,i,j,n):
                    return 0
    return 1
    
def solution(p):
    ans = []
    for li in p:
        ans.append(isPossible(li))
    return ans

                    
        