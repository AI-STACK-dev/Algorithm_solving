numList = list(map(int,list(input())))
numList.sort(reverse=True)

if sum(numList) % 3 != 0 or 0 not in numList:
    print(-1)
else:
    print(*numList,sep='')
    