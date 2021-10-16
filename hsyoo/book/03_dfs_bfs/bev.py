def dfs(y,x):
    if y < 0 or y >= n or x <0 or x>=m:
        return False
    if graph[y][x] == 0:
        graph[y][x] = 1
        dfs(y-1, x)
        dfs(y, x+1)
        dfs(y+1, x)
        dfs(y, x-1)
        return True
    return False

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

cnt = 0
for y in range(n):
    for x in range(m):
        if dfs(y,x) == True:
            cnt +=1
print(cnt)