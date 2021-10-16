from sys import stdin

n,m = list(map(int,stdin.readline().split()))
d = [stdin.readline() for _ in range(n)]
data=[]
for st in d:
    temp =[]
    for c in st:
        if c =='.':
            temp.append(0)
        else:
            temp.append(1)
    data.append(temp)

path_x = [[0, 0,1, 1,1,-1],[0, 0,1,-1,-1,-1]]
path_y = [[1,-1,1,-1,0, 0],[1,-1,0,-1, 1, 0]]

cnt = 0
for i in range(n):
    for j in range(m):
        if data[i][j] == 0:
            continue
        
        # 주변 search
        if i % 2 == 0:
            idx = 1
        else:
            idx = 0

        for dx,dy in zip(path_x[idx],path_y[idx]):
            x = j+dx
            y = i+dy
            if x>=0 and x <= (m-1) and y>=0 and y<=(n-1):
                val = data[y][x]
                if val==0:
                    cnt +=1

print(cnt)
        