import sys; input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    m,n,x,y = map(int,input().rstrip().split())
    flag = True
    while (x<= m*n):
        if x%n == y%n:
            flag = False
            print(x)
            break
        x += m
    if flag:
        print(-1)