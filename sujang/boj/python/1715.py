from sys import stdin
import heapq as hq

n = int(stdin.readline().rstrip())
data = []
for _ in range(n):
    hq.heappush(data,int(stdin.readline().rstrip()))


if n == 1:
    print(0)
else:
    s = 0 
    while len(data) > 1:
        a = hq.heappop(data)
        b = hq.heappop(data)
        s += a+b
        hq.heappush(data,a+b)
    print(s)