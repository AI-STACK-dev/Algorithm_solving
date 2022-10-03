# RGB 구역과 (R-G), B 구역 구분하기
# bfs로 푸는게 합리적. 연결된 connected component를 어떻게 구분할 것이냐? + 방문처리
# R: 1, G: 2, B: 3으로 뒀을 때, 4로 방문처리를 하자. 그리고 for문 돌면서, 4면 pass 4가 아니면 bfs
# 4가 아닐 경우 bfs 들어가기전에 count += 1, 4일 경우 continue

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

r_g_encode = {'R': 1, 'G': 2, 'B':3}
rg_encode = {'R':1, 'G':1, 'B': 2}
n = int(input())
board = []
n_board = []
for _ in range(n):
    temp = list(input())
    tmp_list_r_g = []
    tmp_list_rg = []
    for case in temp:
        tmp_list_r_g.append(r_g_encode[case])
        tmp_list_rg.append(rg_encode[case])
    board.append(tmp_list_r_g)
    n_board.append(tmp_list_rg)

def bfs_r_g(board, start, value):
    queue = deque([(start)])
    board[start[0]][start[1]] = 4

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] != value:
                continue
            else:
                board[ny][nx] = 4
                queue.append((ny, nx))
            
    return board


answer_r_g = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 4:
            continue
        else:
            answer_r_g += 1
            board = bfs_r_g(board, (i,j), board[i][j])

answer_rg = 0
# print(n_board)
for i in range(n):
    for j in range(n):
        if n_board[i][j] == 4:
            continue
        else:
            answer_rg += 1
            n_board = bfs_r_g(n_board, (i,j), n_board[i][j])
print(answer_r_g, answer_rg)
