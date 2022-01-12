import sys; input = sys.stdin.readline

# 입력
n,m = map(int,input().split())
data = [ list(map(int,input().rstrip().split())) for _ in range(n)]
ans = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(i,j,cnt,val):
    global ans,n,m    
    
    # 종료 조건
    if cnt == 4 :
        ans = max(ans, val)
        return

    # search
    for idx in range(4):
        x,y = i + dx[idx], j + dy[idx]
        if (0<=x<n) and (0<=y<m) and visited[x][y] == 0:
            if cnt == 2:
                visited[x][y] = 1
                dfs(i,j,cnt+1,val+data[x][y])
                visited[x][y] = 0

            visited[x][y] = 1
            dfs(x,y,cnt+1,val+data[x][y])
            visited[x][y] = 0



visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        val = data[i][j]
        dfs(i,j,1,val)
        visited[i][j] = 0
print(ans)
