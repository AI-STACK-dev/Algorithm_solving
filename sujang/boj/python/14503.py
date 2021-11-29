import sys; input = sys.stdin.readline

n,m = map(int,input().rstrip().split())
r,c,d = map(int,input().rstrip().split())
field = [list(map(int,input().rstrip().split())) for _ in range(n)]

forward = {0:(0,-1), 1:(1,0), 2:(0,1), 3:(-1,0)}
cnt = 0
while True:
    if field[r][c] == 0:
        cnt += 1
        field[r][c] = 2
    done = False
    # 4방향 모두 스캔
    for i in range(4):
        d = (d-1)%4
        x,y = c+forward[d][0], r+forward[d][1]
        if field[y][x] == 0:
            c,r = x,y
            done = True
            break
    # 뒤로 후진해보자
    if not done:
        D = (d+2)%4
        x,y = c+forward[D][0],r+forward[D][1]
        if field[y][x] == 1:
            break
        else:
            c,r = x,y
print(cnt)
