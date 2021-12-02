from functools import reduce
for _ in range(int(input())):
    ans = 0
    for s in input().split('X'):
        s = len(s)
        if s != 0:
            ans += reduce(lambda x,y: x+y, list(range(1,s+1)))
    print(ans)