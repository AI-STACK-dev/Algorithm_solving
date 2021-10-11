from sys import stdin
from itertools import combinations
import math

n,m = list(map(int,stdin.readline().split()))
data = [list(map(int,stdin.readline().split())) for _ in range(n)]

house,chicken = [],[]
for i in range(n):
    for j in range(n):
        if data[i][j] == 1:
            house.append([i,j])
        if data[i][j] == 2:
            chicken.append([i,j])

distance =[]
for h in house:
    temp_house=[]
    for c in chicken:
        d = abs(c[0]-h[0])+abs(c[1]-h[1])
        temp_house.append(d)
    distance.append(temp_house)

chicken_idx = list(range(len(chicken)))
ans = math.inf
idxss = list(combinations(chicken_idx,m))
for idxs in idxss:
    part = 0
    for d in distance:
        temp = []
        for i in idxs:
            temp.append(d[i])
        part += min(temp)
    ans = min(ans,part)
print(ans)

