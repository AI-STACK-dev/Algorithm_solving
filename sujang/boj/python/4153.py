while True:
    lst = list(map(int,input().split()))
    if min(lst) == 0:
        break
    lst.sort()
    s = lst[0]**2 + lst[1]**2
    if s == lst[2]**2:
        print("right")
    else:
        print("wrong")
