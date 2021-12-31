import sys; input = sys.stdin.readline

# m 은 상어의 수, 이걸로 종료조건 카운트 하자
n,m,k = map(int,input().split())
field = [ [ [0,0] for _ in range(n)] for _ in range(n)]
for i in range(n):
    temp = list(map(int,input().rstrip().split()))
    for j in range(n):
        if temp[j] != 0:
            field[i][j][0] = temp[j]
            field[i][j][1] = k
shark_direction = list(map(int, input().rstrip().split()))
shark_priority = []
for _ in range(m):
    temp = []
    for _ in range(4):
        d = list(map(int,input().rstrip().split()))
        temp.append(d)
    shark_priority.append(temp)

# direction
dx = [-1,1,0,0]
dy = [0,0,-1,1]

# shark's next location
def next_move(x,y):
    global n
    id = field[x][y][0]
    now_direction = shark_direction[id-1]
    empty = []
    same_smell = []
    for d in shark_priority[id-1][now_direction-1]:
        nx,ny = dx[d-1],dy[d-1]
        a,b = x+nx,y+ny
        if 0<=a<n and 0<=b<n:
            if field[a][b][0] == 0:
                empty.append([a,b,d])
            elif field[a][b][0] == id:
                same_smell.append([a,b,d])
    if empty:
        return empty[0],id
    elif same_smell:
        return same_smell[0],id
    else:
        return [x,y,now_direction],id


# let's go
M = m
time = 0
while True:
    s = [None]*m
    # field를 탐색 하며, 상어 이동
    for i in range(n):
        for j in range(n):
            a,b = field[i][j]
            # 상어가 있다면
            if b == k:
                e,id = next_move(i,j)
                s[id-1] = e

    for i in range(n):
        for j in range(n):
            a,b = field[i][j]
            # 만약 냄새만 있다면
            if 0 < b <= k :
                field[i][j][1] -= 1
                if field[i][j][1] == 0:
                    field[i][j][0] = 0

    # 움직인 상어 위치 업데이트
    for idx in range(m):
        if s[idx] != None:
            x,y,d = s[idx]
            # 상어가 있다면, 잡아먹힌거임
            if field[x][y][1] == k:
                M -= 1
                continue
            # 상어가 없다면
            field[x][y][0] = idx+1
            field[x][y][1] = k
            shark_direction[idx] = d
    time += 1
    if time > 1000:
        time = -1
        break

    if M == 1:
        break
    
print(time) 