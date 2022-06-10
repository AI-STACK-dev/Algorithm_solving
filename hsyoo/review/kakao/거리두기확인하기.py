# from collections import deque
# import copy
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
# def str2list(place):
#     board = []
#     for temp in place:
#         for idx, case in enumerate(['O','X','P']):
#             temp = temp.replace(case, str(idx))
#         board.append(list(map(int, temp)))
#     return board

# def bfs(board, i, j):
#     n_board = copy.deepcopy(board)
#     print(board)
#     queue = deque([(i, j, 0, False)])
#     while queue:
#         print(queue)
#         y, x, cost, p_exist = queue.popleft()
#         if p_exist == True:
#             break
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             # print(ny, nx)
#             if ny < 0 or nx < 0 or ny >=5 or nx >= 5:
#                 continue
#             if n_board[ny][nx] == 1:
#                 continue
#             if n_board[ny][nx] == 2:
#                 queue.append((ny, nx, cost + 1, True))
#                 n_board[ny][nx] = 1
#             if n_board[ny][nx] == 0:
#                 queue.append((ny, nx, cost + 1, False))
#                 n_board[ny][nx] = 1

#     print(p_exist, cost)
#     if p_exist == False:
#         return True
#     elif p_exist == True and cost > 2:
#         return True
#     else:
#         return False
            
# def solution(places):
#     answer = []
#     for place in places:
#         board = str2list(place)
#         flag = True
#         for i in range(5):
#             for j in range(5):
#                 if board[i][j] == 2:
#                    flag = flag and bfs(board, i, j)
#         break
#         if flag == True:
#             answer.append(1)
#         else:
#             answer.append(0) 
#     return answer

from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(place):
    start = []
    for i in range(5):
        for j in range(5):
            if place[i][j] == 'P':
                start.append((i,j))
    
    for coord in start:
        queue = deque([coord])
        visited = [[0] * 5 for _ in range(5)]
        distance = [[0] * 5 for _ in range(5)]
        visited[coord[0]][coord[1]] = 1

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                if 0 <= ny < 5 and 0 <= nx < 5 and visited[ny][nx] == 0:
                    if place[ny][nx] == 'O':
                        visited[ny][nx] = 1
                        distance[ny][nx] = distance[y][x] + 1
                        queue.append((ny, nx))
                    elif place[ny][nx] == 'P' and distance[y][x] <= 1:
                        return 0
    return 1

def solution(places):
    answer = []
    for place in places:
        answer.append(bfs(place))
    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]	))