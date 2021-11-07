from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


distances = [-1] * (n + 1)
distances[x] = 0

queue = deque([x])
while queue:
    v = queue.popleft()
    for i in graph[v]:
        if distances[i] == -1:
            distances[i] = distances[v] + 1
            queue.append(i)

check = True
for i in range(1, n + 1):
    if distances[i] == k:
        print(i)
        check = False

if check: print(-1)