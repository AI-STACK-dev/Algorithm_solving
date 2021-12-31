import heapq
import sys; input=sys.stdin.readline

n = int(input())
h = []
for _ in range(n):
    num = int(input().rstrip())
    if num == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(num)
    else:
        heapq.heappush(h,num)
