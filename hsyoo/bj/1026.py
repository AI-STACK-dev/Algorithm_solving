import heapq

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
q = []
for i in range(n):
    heapq.heappush(q, -b[i])
result = 0
for i in range(n):
    result += (a[i] * -heapq.heappop(q))
print(result)