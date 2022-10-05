from collections import deque 

n, m = map(int, input().split())
ladder = {i+1:x+1 for i, x in enumerate(range(100))}
snake = {i+1:x+1 for i, x in enumerate(range(100))}

for _ in range(n):
    from_, to_ = map(int, input().split())
    ladder[from_] = to_

for _ in range(m):
    from_, to_ = map(int, input().split())
    snake[from_] = to_

def bfs(start):
    queue = deque([(start, 0)])
    visited = [False] * 101
    visited[start] = True
    
    while queue:
        y, value = queue.popleft()
        if y == 100:
            return value
        for i in range(1, 7):
            ny = y + i
            if ny > 100:
                continue
            ny = ladder[ny]
            ny = snake[ny]
            if visited[ny] != True:
                queue.append((ny, value + 1))
                visited[ny] = True
            
    

answer = bfs(1)
print(answer)
