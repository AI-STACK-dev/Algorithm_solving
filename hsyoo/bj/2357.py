import heapq
import copy
import sys

input = sys.stdin.readline
n,m = map(int, input().split())
ary = []
for _ in range(n):
    ary.append(int(input()))

result = []
for _ in range(m):
    a,b = map(int, input().split())
    q = copy.deepcopy(ary[a-1:b])
    temp = copy.deepcopy(ary[a-1:b])
    heapq.heapify(q)
    # print(heapq.heappop(q), end = ' ')
    min_ = heapq.heappop(q)

    q = []
    for case in temp:
        q.append(-case)
    heapq.heapify(q)
    max_ = -heapq.heappop(q)
    result.append((min_, max_))

for min_, max_ in result:
    print(min_, max_)
    
