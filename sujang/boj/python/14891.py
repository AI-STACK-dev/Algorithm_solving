from sys import stdin
from collections import deque
cycle = [list(map(int,list(stdin.readline().rstrip()))) for _ in range(4)] 
n = int(stdin.readline().rstrip())
data = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(n):
    chain = []
    target, direction = data[i]
    # check chain right side
    d = direction
    for s in range(target,4):
        if cycle[s-1][2] !=  cycle[s][6]:
            d *= (-1)
            chain.append([s,d])
        else:
            break
    # check chain left side
    d = direction
    for s in range(target-2,-1,-1):
        if cycle[s][2] !=  cycle[s+1][6]:
            d *= (-1)
            chain.append([s,d])
        else:
            break
    chain.append([target-1,direction])

    for t,d in chain:
        # change direction
        if d == 1:
            end = cycle[t].pop()
            cycle[t].insert(0,end)
        else:
            front = cycle[t].pop(0)
            cycle[t].append(front)

ans = 0
for i in range(4):
    if cycle[i][0]==1:
        ans += 2**i 
print(ans)
