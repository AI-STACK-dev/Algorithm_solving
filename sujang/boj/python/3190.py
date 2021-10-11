import sys
from sys import stdin

n = int(stdin.readline())
k = int(stdin.readline())
app = [list(map(int,stdin.readline().split())) for _ in range(k)]
l = int(stdin.readline())
mov = [stdin.readline().split() for _ in range(l)]

## field 설정
field = [[1]*(n+2) if x ==0 or x ==(n+1) else [0]*(n+2) for x in range(n+2)]
for i in range(n+2):
    field[i][0] = 1
    field[i][n+1] = 1

apple_map = [[0]*(n+2) for _ in range(n+2)]
for a in app:
    apple_map[a[0]][a[1]] = 1

move_dict = {}
for m in mov:
    if m[1] == 'D':
        move_dict[int(m[0])] = 1
    else:
        move_dict[int(m[0])] = -1

## 방향 설정
dx = [0,1, 0,-1]
dy = [1,0,-1, 0]
direction = 0

## 초기 설정
field[1][1] = 1
trace = [[1,1]]
head = [1,1]
time = 0

while True:
    time += 1
    next_head = [head[0]+dx[direction],head[1]+dy[direction]]

    ## 벽이거나 몸이면 죽는다.
    if field[next_head[0]][next_head[1]] == 1 :
        print(time)
        sys.exit(0)
        
    ## 다음 머리에 애플이 없다면
    if apple_map[next_head[0]][next_head[1]] != 1:
        x,y = trace.pop(0)
        field[x][y] = 0
    else:
        apple_map[next_head[0]][next_head[1]] = 0
    trace.append(next_head)
    field[next_head[0]][next_head[1]] = 1
    head = next_head

    ## 뱀의 방향을 변경할 시간이면
    if time in move_dict:
        direction += move_dict[time]
        direction %= 4
    


