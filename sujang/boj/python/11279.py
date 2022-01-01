import heapq as hp
import sys; input = sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    num = int(input())
    if num == 0:
        if h:
            print(-hp.heappop(h))
        else:
            print(num)
    else:
        hp.heappush(h,-num)
