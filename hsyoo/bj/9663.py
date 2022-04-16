# n = int(input())
# graph = [[0] * n for _ in range(n)]
# dy = [-1, 0, 1, 0, -1, 1, 1, -1]
# dx = [0, 1, 0, -1, 1, 1, -1, -1]

# def dfs(graph, coord, cnt):
#     y, x, direc = coord[0], coord[1], coord[2]
#     graph[y][x] = cnt
#     if direc == None:
#         for i in range(8):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if ny < 0 or nx < 0 or ny >= n or nx >= n:
#                 continue
#             dfs(graph, (ny,nx, i), cnt)
#     else:
#         ny = y + dy[direc]
#         nx = x + dx[direc]
#         if ny < 0 or nx < 0 or ny >= n or nx >= n:
#             return
#         dfs(graph, (ny,nx, direc), cnt)

# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 0:
#             cnt += 1
#             dfs(graph, (i,j, None), cnt)
# print(cnt)

n = int(input())
result = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True
    
def n_queens(x):
    global result
    if x == n:
        result += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x+1)
n_queens(0)
print(result)