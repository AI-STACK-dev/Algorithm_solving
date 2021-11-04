from sys import stdin

n,m,x,y,k = map(int,stdin.readline().rstrip().split())
field = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
cmd = list(map(int,stdin.readline().rstrip().split()))

dice =[ [0],
      [0,0,0,0],
        [0]
]
dx = [0, 0,-1,1]
dy = [1,-1, 0,0]

for c in cmd:
    # coordinate update
    if 0<=x+dx[c-1]<n and 0<=y+dy[c-1]<m:
        x += dx[c-1]
        y += dy[c-1]
    else:
        continue

    # dice move
    if c == 1:
        end = dice[1].pop()
        dice[1].insert(0,end)
    elif c == 2:
        front = dice[1].pop(0)
        dice[1].append(front)
    elif c == 3:
        one,two,three,four = dice[1][1],dice[2][0],dice[1][3],dice[0][0]
        dice[1][1],dice[2][0],dice[1][3],dice[0][0] = two,three,four,one
    else:
        one,two,three,four = dice[1][1],dice[2][0],dice[1][3],dice[0][0]
        dice[1][1],dice[2][0],dice[1][3],dice[0][0] = four,one,two,three

    if field[x][y] == 0:
        field[x][y] = dice[1][3]
    else:
        dice[1][3] = field[x][y]
        field[x][y] = 0
    print(dice[1][1])