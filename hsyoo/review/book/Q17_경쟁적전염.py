from collections import defaultdict, deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N, K = map(int, input().split())
coord = defaultdict(list)
board = []
for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(N):
        if temp[j] != 0:
            coord[temp[j]].append((i,j, 0))
    board.append(temp)

S, target_y, target_x = map(int, input().split())

def bfs(board, k, s):
    new_list = []
    queue = deque(coord[k])
    
    while queue:
        y, x, cost = queue.popleft()
        if cost == s + 1:
            break
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= N or nx >= N:
                continue
            if board[ny][nx] == 0:
                queue.append((ny,nx,cost+1))
                new_list.append((ny,nx,cost+1))
                board[ny][nx] = k

    return board, new_list

for s in range(S):
    for k in range(1, K+1):
        board, new_list = bfs(board, k, s)
        coord[k] = new_list
print(board[target_y - 1][target_x - 1])
