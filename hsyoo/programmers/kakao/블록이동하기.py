# from collections import deque

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
# check_y = [-1,1,1,-1]
# check_x = [1,1,-1,-1]

# def state_check(y, x, y_, x_):
#     if [y_, x_] == [y-1, x]:
#         return 0
#     elif [y_,x_] == [y, x+1]:
#         return 1
#     elif [y_,x_] == [y+1, x]:
#         return 2
#     elif [y_, x_] == [y, x-1]:
#         return 3
# def rotate_right(y, x, state):
#     state += 1
#     if state == 4:
#         state = 0
#     y_ = y + dy[state]
#     x_ = x + dx[state]
#     return (y, x, y_, x_, state)

# def rotate_left(y, x, state):
#     state -= 1
#     if state == -1:
#         state = 3
#     y_ = y + dy[state]
#     x_ = x + dx[state]
#     return (y, x, y_, x_, state)

# def checking_right(n, board, y,x,state):
#     ny = y + check_y[state]
#     nx = x + check_x[state]
#     if ny < 0 or nx < 0 or ny >= n or nx >= n:
#         return False
#     if board[ny][nx] == 1:
#         return False
#     return True

# def cheking_left(n, board, y, x, state):
#     ny = y + check_y[3-state]
#     nx = x + check_x[3-state]
#     if ny < 0 or nx < 0 or ny >= n or nx >= n:
#         return False
#     if board[ny][nx] == 1:
#         return False
#     return True
    
# def solution(board):
#     answer = 0
#     n = len(board)
#     # y, x, state, cost
#     queue = deque([(0, 0, 1, 0)])
#     while queue:
#         y,x,state, cost = queue.popleft()
        
    

#     return answer

from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        pos1_next_x, pos1_next_y, pos2_next_x, pos2_next_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if board[pos1_next_x][pos1_next_y] == 0 and board[pos2_next_x][pos2_next_y] == 0:
            next_pos.append(set([(pos1_next_x, pos1_next_y), (pos2_next_x, pos2_next_y)]))
    if pos1_x == pos2_x:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[pos1_x + i][pos1_y] == 0 and board[pos2_x + i][pos2_y] == 0: # 위쪽 혹은 아래쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x + i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x + i, pos2_y)})
    elif pos1_y == pos2_y:
        for i in [-1, 1]:
            if board[pos1_x][pos1_y + i] == 0 and board[pos2_x][pos2_y + i] == 0: # 왼쪽 혹은 오른쪽 두 칸이 모두 비어 있다면
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y + i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y + i)})

    return next_pos

def solution(board):
    n = len(board)
    new_board = [[1] * (n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    
    q = deque()
    visited = []
    pos = set([(1,1), (1,2)])
    q.append((pos, 0))
    visited.append(pos)
    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    return 0