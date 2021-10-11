import heapq as hp
from sys import stdin

# 입력
n,k = map(int,stdin.readline().split())
jewel = []
for _ in range(n):
    w,v = map(int,stdin.readline().split())
    hp.heappush(jewel,[w,v])
bag = [int(stdin.readline()) for _ in range(k)]
bag.sort()

temp = []
val = 0
for b in bag:
    while jewel and b >= jewel[0][0]:
        w,v = hp.heappop(jewel)
        hp.heappush(temp, -v)
    if temp:  
        val -= hp.heappop(temp)
    elif not jewel:
        break
print(val)
