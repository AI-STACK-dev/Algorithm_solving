from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs(array, y,x):
    queue = deque([(y,x)])
    while queue:
        v = queue.popleft()
        value = ary[v[0]][v[1]]
        for i in range(4):
            ny = v[0] + dy[i]
            nx = v[1] + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >=m:
                continue
            if ary[ny][nx] == 0 or ary[ny][nx] > 1:
                continue
            else:
                ary[ny][nx] = value + 1
                queue.append((ny,nx))
    return ary[n-1][m-1]
n,m = map(int, input().split())
ary = []
for _ in range(n):
    ary.append(list(map(int, input())))

result = bfs(ary, 0, 0)
print(result)