from collections import deque

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
direc = 1

def direc_change(c):
    global direc

    if c == 'L':
        direc -= 1
        if direc == -1:
            direc = 3
    elif c == 'D':
        direc += 1
        if direc == 4:
            direc = 0


n = int(input())
k = int(input())
board = [[0] * n for _ in range(n)]
# snake는 queue에서, apple은 2로
for _ in range(k):
   i, j = map(int, input().split())
   board[i-1][j-1] = 2

L = int(input())
direc_queue = deque([])
for _ in range(L):
    x, c = input().split()
    x = int(x)
    direc_queue.append((x,c))

for case in board:
    print(case)

ny,nx = 0,0
body = deque([])
answer = 1
while True:
    ny = ny + dy[direc]
    nx = nx + dx[direc]
    print(ny, nx, body)
    if ny < 0 or nx < 0 or ny >= n or nx >= n:
        break
    if (ny,nx) in body:
        break
    if board[ny][nx] == 2:
        body.append((ny,nx))
        board[ny][nx] = 0

    elif board[ny][nx] == 0:
         body.append((ny,nx))
         body.popleft()

    if len(direc_queue) > 0 and answer == direc_queue[0][0]:
        x, c = direc_queue.popleft()
        direc_change(c)
    answer +=1
print(answer)
