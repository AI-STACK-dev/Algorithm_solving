from collections import deque

n,k = map(int,input().split())
visited = [[-1,0] for _ in range(100001)]

def bfs(n):
    q= deque([n])
    visited[n][0] = 0
    visited[n][1] = 1

    while q:
        x = q.popleft()
        for i in [x-1,x+1,x*2]:
            if 0<= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] = visited[x][1]
                    q.append(i)

                elif visited[i][0] == visited[x][0]+1:
                    visited[i][1] += visited[x][1]

bfs(n)
print(visited[k][0])
print(visited[k][1])