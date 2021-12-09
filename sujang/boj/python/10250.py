tc = int(input())
for _ in range(tc):
    h,w,n = map(int,input().split())
    back = n // h + 1
    front = n % h
    if n % h == 0:
        back = n//h
        front = h
    print(str(front*100+back))