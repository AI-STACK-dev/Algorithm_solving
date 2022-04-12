from collections import deque
import copy

v = int(input())
indegree = [0] * (v+1)
graph = [[] for _ in range(v+1)]
time = [0] * (v+1)
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for x in data[1:-1]:
        indegree[i] += 1
        graph[x].append(i)


def topology_sort():
    q = deque()
    result = copy.deepcopy(time)

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        now = q.popleft()
        # result.append(now)
        for i in graph[now]:
            result[i] = max(result[i], result[now] + time[i])
            indegree[i] -= 1
            if indegree[i] ==0:
                q.append(i)
    for i in range(1,v+1):
        print(result[i])
topology_sort()