import sys
from sys import stdin

def makeTree(r,c,n):
    x = [-1,-1,-1, 0,0, 1,1,1]
    y = [-1, 0, 1,-1,1,-1,0,1]
    ls = []
    for xx, yy in zip(x,y):
        X = r+xx
        Y = c+yy
        if X >= 0 and X <= n-1 and  Y >= 0 and Y <= n-1:
            ls.append([X,Y])
    return ls

n,m,K = map(int,stdin.readline().split())
s2d2 = [list(map(int, stdin.readline().split())) for _ in range(n)]
# tree의 3차원 배열
tree = [[[] for __ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y,z = map(int, stdin.readline().split())
    tree[x-1][y-1].append(z)
land = [[5]*n for _ in range(n)]

for _ in range(K):
    # in Spring and Summer
    for i in range(n):
        for j in range(n):
            if tree[i][j]:
                nut = land[i][j]
                tree[i][j].sort()
                l,d = [],0
                for vv in tree[i][j]:
                    if nut  >= vv:
                        nut -= vv
                        l.append(vv+1)
                    else:
                        d += (vv//2)
                tree[i][j] = l
                land[i][j] = nut + d
    # exit
    if not tree:
        print(0)
        sys.exit()
    # in Fall and winter
    for i in range(n):
        for j in range(n):
            land[i][j] += s2d2[i][j]
            if tree[i][j]:
                for t in tree[i][j]:
                    if t % 5 == 0:
                        ls = makeTree(i,j,n)
                        for l in ls:
                            tree[l[0]][l[1]].append(1)
            
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += len(tree[i][j])
print(cnt)




