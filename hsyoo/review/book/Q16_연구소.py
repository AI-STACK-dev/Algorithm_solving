from collections import deque
from itertools import combinations
from copy import deepcopy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(board, starts):
    n = len(board)
    m = len(board[0])
    q = deque(starts)
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if board[ny][nx] != 0:
                    continue
                else:
                    board[ny][nx] = 2
                    q.append((ny, nx))

    cnt = 0
    for i in range(n):
        for j in range(m):
           if board[i][j] == 0:
               cnt += 1
    return cnt

n, m = map(int, input().split())
board = []
zeros = []
virus = []
for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 0:
            zeros.append((i, j))
        elif temp[j] == 2:
            virus.append((i, j))
    board.append(temp)

comb = list(combinations(zeros, 3))
result = []
for case in comb:
    n_board = deepcopy(board)
    for i in range(3):
        n_board[case[i][0]][case[i][1]] = 1
    result.append(bfs(n_board, virus))
print(max(result))