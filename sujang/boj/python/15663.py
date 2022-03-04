n,m = map(int, input().split())
data = list(map(int,input().split()))
data.sort()

visited = [False] * n
ans = []

def dfs(depth):
    if depth == m:
        print(*ans)
        return
    prev = 0
    for i in range(n):
        if not visited[i] and data[i] != prev:
            visited[i] = True
            prev = data[i]
            ans.append(data[i])
            dfs(depth+1)
            visited[i] = False
            ans.pop()

dfs(0)
