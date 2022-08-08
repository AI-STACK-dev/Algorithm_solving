# from collections import deque
# from itertools import combinations
# from copy import deepcopy

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# n,m = map(int, input().split())
# board = []
# start_points = []
# cp = []
# for i in range(n):
#     temp = list(map(int, input().split()))
#     for j in range(n):
#         if temp[j] == 1:
#             start_points.append((i,j,0))
#         elif temp[j] == 2:
#             cp.append((i,j))
#     temp = list(map(str, temp))
#     temp = ''.join(temp)
#     temp = temp.replace('2', '0')
#     temp = list(map(int, temp))
#     board.append(temp)

# def bfs(board, start_point):
#     queue = deque([])
#     queue.append(start_point)
#     while queue:
#         y,x, cost = queue.popleft()
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or nx < 0 or ny >= n or nx >= n:
#                 continue
#             if 0 <= board[ny][nx] <= 2:
#                 if 0<=board[ny][nx]<=1:
#                     queue.append((ny,nx, cost + 1))
#                     board[ny][nx] = 3
#                 elif board[ny][nx] == 2:
#                     return cost + 1


# comb = []
# comb.extend(list(combinations(cp, m)))

# answer = []
# for cases in comb:
#     # chicken point -> cases 특정 m개의 치킨집만 고르기
#     n_board = deepcopy(board)
#     for case in cases:
#         n_board[case[0]][case[1]] = 2

#     chicken_dists = []
#     for start_point in start_points:
#         temp = deepcopy(n_board)
#         dist = bfs(temp, start_point)
#         chicken_dists.append(dist)
#         print(start_point, dist, '\n\n')
#     answer.append(sum(chicken_dists))
# print(min(answer))

"""
-> 시간초과
"""

from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r,c))
        elif data[c] == 2:
            chicken.append((r,c))

candidates = list(combinations(chicken, m))

def get_sum(candidate):
    result = 0
    for hx, hy in house:
        temp = 1e9
        for cx, cy in candidate:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))
print(result)