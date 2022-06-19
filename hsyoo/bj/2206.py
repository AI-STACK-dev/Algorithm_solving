from collections import deque
import sys
import copy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(n, m, board):
    walls = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                walls.append((i,j))
    answer = []
    for wall in walls:
        n_board = copy.deepcopy(board)
        n_board[wall[0]][wall[1]] = 0
        queue = deque([(0,0,1)])
        while queue:
            y, x, cost = queue.popleft()
            if y == n-1 and x == m-1:
                answer.append(cost)
                break
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0<=ny<n and 0 <= nx < m and n_board[ny][nx] == 0:
                    queue.append((ny, nx, cost + 1))
                    n_board[ny][nx] = 1
    if len(answer) == 0:
        return -1
    else:
        return min(answer)

n,m = map(int, input().split())
input = sys.stdin.readline
board = []
for _ in range(n):
    temp = list(map(int, list(input().rstrip())))
    board.append(temp)

print(bfs(n,m,board))

