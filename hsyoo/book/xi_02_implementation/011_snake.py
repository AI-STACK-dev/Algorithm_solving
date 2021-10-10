n = int(input())
k = int(input())
apple = []
time = []
time_direc = []
body = [(1,1)]
for _ in range(k):
    a,b = map(int, input().split())
    apple.append((a,b))
l = int(input())
for _ in range(l):
    a,b = input().split()
    time.append(int(a))
    time_direc.append(b)
cnt = 1
direc = 1
dy = [-1,0,1,0]
dx = [0,1,0,-1]
y,x = 1,1
def turn_left():
    global direc
    direc -=1
    if direc == -1:
        direc = 3
def turn_right():
    global direc
    direc += 1
    if direc == 4:
        direc = 0

while True:
    y = y + dy[direc]
    x = x + dx[direc]
    head = (y,x)
    print(f"{cnt} : {head}")
    print(f"body : {body}")
    if head in body:
        cnt +=1
        break
    if head in apple:
        body.append(head)
    else:
        try:
            body.append(head)
            del body[0]
        except:
            pass
    cnt += 1
    if y<=0 or y>=n:
        cnt+=1
        break
    if x<=0 or x>=n:
        cnt+=1
        break
    if cnt in time:
        temp = time.index(cnt)
        if time_direc[temp] == 'L':
            turn_left()
        elif time_direc[temp] == 'D':
            turn_right()
print(cnt)