from sys import stdin

t = int(stdin.readline().rstrip())
ans = []
for _ in range(t):
    x_1,y_1,x_2,y_2 = map(int,stdin.readline().rstrip().split())
    n = int(stdin.readline().rstrip())
    cnt = 0
    for _ in range(n):
        cx,cy,r = map(int,stdin.readline().rstrip().split())
        distance_1 = (cx-x_1)**2 + (cy-y_1)**2
        distance_2 = (cx-x_2)**2 + (cy-y_2)**2
        if (distance_1 - r**2) * (distance_2 - r**2) < 0:
            cnt += 1
    ans.append(cnt)
print(*ans,sep='\n')