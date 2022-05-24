from collections import deque
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solution(board):
    INF = int(1e9)
    n = len(board)
    answer = INF
    dist = [[[INF for _ in range(n)] for _ in range(n)] for _ in range(4)]
    queue = deque([])
    queue.append((0, 0, 0, 1))
    queue.append((0, 0, 0, 2))
    while queue:
        y, x, cost, direc = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] == 0:
                n_cost = cost + 100
                if direc != i:
                    n_cost +=  500
                if n_cost < dist[i][ny][nx]:
                    dist[i][ny][nx] = n_cost
                    if ny == n-1 and nx == n-1:
                        continue
                    queue.append((ny, nx, n_cost, i))
    for i in range(4):
        answer = min(answer, dist[i][n-1][n-1])
    return answer

# import sys
# import collections
# def solution(board):
#     INF=sys.maxsize
#     n=len(board)
#     answer = INF
#     # dd=[0, 1, 2, 3]
#     dy=[0, 1, 0, -1]
#     dx=[1, 0, -1, 0]
#     dist=[[[INF for _ in range(len(board[0]))] for _ in range(len(board))] for _ in range(4)]
#     q=collections.deque()
#     q.append([0, 0, 0, 0])
#     q.append([0, 0, 0, 1])
#     while q:
#         y, x, cost, d=q.popleft()
#         for i in range(4):
#             ny=y+dy[i]
#             nx=x+dx[i]
#             if 0<=ny<n and 0<=nx<n and board[ny][nx]==0:
#                 n_cost=cost+1
#                 if d!=i:
#                     n_cost+=5
#                 if dist[i][ny][nx]>n_cost:
#                     dist[i][ny][nx]=n_cost
#                     if ny==n-1 and nx==n-1:
#                         continue
#                     q.append([ny, nx, n_cost, i])
#     for i in range(4):
#         answer=min(answer, dist[i][n-1][n-1])
#     answer*=100
#     return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))