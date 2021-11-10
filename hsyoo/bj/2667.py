from collections import deque

dy = [-1,0,1,0]
dx = [0,1,0,-1]
def bfs(ary, y, x):
    ary[y][x] += 1
    queue = deque([(y,x)])
    cnt = 0
    while queue:
        v = queue.popleft()
        cnt+=1
        for i in range(4):
            ny = v[0] + dy[i]
            nx = v[1] + dx[i]
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if ary[ny][nx] == 1:
                queue.append((ny,nx))
                ary[ny][nx] += 1

    return cnt

n = int(input())
ary = []
for i in range(n):
    ary.append(list(map(int, input())))

result = []
for y in range(n):
    for x in range(n):
        if ary[y][x] == 0 or ary[y][x] > 1:
            continue
        else:
            result.append(bfs(ary, y, x))
print(len(result))
result.sort()
for case in result:
    print(case)
