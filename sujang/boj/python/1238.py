from collections import defaultdict
import sys;input = sys.stdin.readline
import heapq as hp

n,m,x = map(int,input().split())

g = defaultdict(list)

for _ in range(m):
    a,b,w = map(int,input().split())
    g[a].append((b,w))


def dijks(startIdx):
    h = []
    hp.heappush(h,(0, startIdx))
    temp = {}
    while h:
        weight, idx = hp.heappop(h)
        if idx not in temp:
            temp[idx] = weight
            for v,w in g[idx]:
                hp.heappush(h,(weight+w, v))
    return temp
    
dicts = []
for i in range(1,n+1):
    dicts.append(dijks(i))

ans = 0
for i in range(1,n+1):
    if i == x:
        continue
    ans = max(dicts[i-1][x]+dicts[x-1][i] , ans)

print(ans)
