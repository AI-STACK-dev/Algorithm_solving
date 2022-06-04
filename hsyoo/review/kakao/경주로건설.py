from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def solution(board):
    INF = int(1e9)
    answer = INF
    n = len(board)
    graph = [[[INF for _ in range(n)] for _ in range(n)] for _ in range(4)]
    # y, x, cost, direction 순서
    queue = deque([])
    queue.append((0, 0, 0, 1))
    queue.append((0, 0, 0, 2))
    while queue:
        y, x, cost, direction = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] == 0:
                n_cost = cost + 100
                if direction != i:
                    n_cost += 500
                if n_cost < graph[i][ny][nx]:
                    graph[i][ny][nx] = n_cost
                    if ny == n-1 and nx == n-1:
                        continue
                    queue.append((ny, nx, n_cost, i))
    for i in range(4):
        answer = min(answer, graph[i][n-1][n-1])
    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))