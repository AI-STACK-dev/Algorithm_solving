import sys;input = sys.stdin.readline
from itertools import combinations

n = int(input())
cnt = n//2
all = list(range(n))
data = [ list(map(int,input().split())) for _ in range(n)]

ans = int(1e9)
for a in combinations(list(range(n)), cnt):
    start = link = 0
    b = list(set(all) - set(a))
    for r in combinations(a,2):
        start += data[r[0]][r[1]]
        start += data[r[1]][r[0]]
    for r in combinations(b,2):
        link += data[r[0]][r[1]]
        link += data[r[1]][r[0]]
    ans = min(ans,abs(start - link))
print(ans)
