import copy

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [ 0, -1,-1,-1, 0, 1, 1, 1]

def get_possible_pos(data,x,y):
    pos = []
    d = data[x][y][1]
    for i in range(4):
        x += dx[d]
        y += dy[d]
        if 0<=x<4 and 0<=y<4 and 1<= data[x][y][0] <= 16:
            pos.append([x,y])
    return pos


def find_fish(data,idx):
    for i in range(4):
        for j in range(4):
            if data[i][j][0] == idx:
                return (i,j)
    return None

def move_all_fishes(data,x,y):
    for i in range(1,17):
        pos = find_fish(data,i)
        if pos != None:
            a,b = pos[0],pos[1]
            d = data[a][b][1]
            for j in range(8):
                aa = a + dx[d]
                bb = b + dy[d]
                if 0 <= aa < 4 and 0<= bb < 4:
                    if not (aa == x and bb == y):
                        data[a][b][0], data[aa][bb][0] = data[aa][bb][0], data[a][b][0]
                        data[a][b][1] = data[aa][bb][1]
                        data[aa][bb][1] = d
                        break
                d = (d+1) % 8

def dfs(data, x, y, total):
    global result
    data = copy.deepcopy(data)

    num = data[x][y][0]
    data[x][y][0] = -1

    move_all_fishes(data,x,y)

    positions = get_possible_pos(data,x,y)

    result = max(result, total+num)
    for nx,ny in positions:
        dfs(data,nx,ny,total+num)


data = [[None] * 4 for _ in range(4)]

for i in range(4):
    d = list(map(int,input().split()))
    for j in range(4):
        num = d[2*j]
        dir = d[2*j+1]-1
        data[i][j] = [num,dir]

result = 0
dfs(data,0,0,0)
print(result)