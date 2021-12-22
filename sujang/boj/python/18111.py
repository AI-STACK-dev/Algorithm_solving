import sys; input = sys.stdin.readline
n,m,b = map(int,input().split())
field = [ list(map(int,input().split())) for _ in range(n) ]

ans = [int(1e9),0]
for lvl in range(257):
    time = 0
    b_avail = b
    for i in range(n):
        for j in range(m):
            val = field[i][j]
            b_avail += (val-lvl)
            if val > lvl:
                time += 2*(val-lvl)
            elif val < lvl:
                time += (lvl-val)
    if b_avail >=0 and time <= ans[0]:        
        ans = [time,lvl]
print(*ans)