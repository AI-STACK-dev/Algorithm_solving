import sys; input = sys.stdin.readline
from collections import deque

def topology_sort():
    q = deque()
    for i in range(1,n+1):
        if indegree[i] == 0:
            q.append(i)

    result = []
    for i in range(n):
        if len(q) == 0:
            return 'IMPOSSIBLE'
        if len(q) > 1:
            return '?'
        now = q.popleft()
        result.append(now)
        for j in range(1,n+1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    q.append(j)
    return result


# 테스트 케이스 개수
ans = []
t = int(input())
for _ in range(t):
    # 변수 설정
    n = int(input())
    graph = [[0]*(n+1) for _ in range(n+1)]
    indegree = [0]*(n+1)

    # 작년 상태 반영
    prev = list(map(int,input().split()))
    for i in range(n):
        for j in range(i+1,n):
            graph[prev[i]][prev[j]] = 1
            indegree[prev[j]] +=1

    m = int(input())
    for _ in range(m):
        a,b = map(int,input().split())
        if graph[a][b]:
            graph[b][a] = 1
            graph[a][b] = 0
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[b][a] = 0
            graph[a][b] = 1
            indegree[a] -= 1
            indegree[b] += 1
    
    ans.append(topology_sort())
for a in ans:
    if type(a) is str:
        print(a)
    else:
        print(*a)