from sys import stdin
import heapq as hp

n = int(stdin.readline())
data = []
for _ in range(n):
    p,d = map(int,stdin.readline().split())
    hp.heappush(data, [-p,d])

new_dict = {}
for _ in range(1,n+1):
    p,d = hp.heappop(data)
    if d in new_dict:
        for i in range(d-1,0,-1):
            if not i in new_dict:
                new_dict[i] = p
                break
    else:
        new_dict[d] = p
print(-sum(list(new_dict.values())))
