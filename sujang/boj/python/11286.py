import sys; input = sys.stdin.readline
import heapq as hp

data = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if data:
            print(hp.heappop(data)[1])
        else:
            print(0)
    else:
        hp.heappush(data,[abs(num),num])