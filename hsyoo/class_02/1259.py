while True:
    ary = list(input())
    if len(ary) == 1 and int(ary[0]) == 0:
        break
    half = len(ary)//2
    flag = True
    for i in range(half):
        if ary[i] != ary[-(1+i)]:
            flag = False
    if flag:
        print('yes')
    else:
        print('no')
    
    
# print(list(input()))