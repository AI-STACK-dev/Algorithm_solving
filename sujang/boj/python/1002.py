from sys import stdin

t = int(stdin.readline().rstrip())
ans = []
for _ in range(t):
    x,y,r,a,b,l = map(int,stdin.readline().rstrip().split())
    distance = (x-a)**2 + (y-b)**2

    # r이 무조건 크다고 가정
    if l > r: 
        l,r = r,l

    cnt = 0
    # 한 점에서 만나는 경우
    if distance == (r+l)**2: 
        cnt = 1
    # 두 점에서 만나는 경우
    elif (r-l)**2< distance < (r+l)**2:
        cnt = 2
    # 아예 안 만나는 경우
    elif distance > (r+l)**2:
        cnt = 0
    # 한 점에서 내접하는 경우
    elif (r-l)**2 == distance and distance !=0:
        cnt = 1
    # 한 원이 다른 원 안에 있을 경우
    elif distance < (r-l)**2:
        cnt = 0
    # 두 원이 같은 경우
    elif distance ==0 and r==l:
        cnt = -1
    ans.append(cnt)
print(*ans,sep='\n')