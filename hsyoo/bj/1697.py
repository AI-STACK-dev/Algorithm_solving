"""from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001
def bfs(n,k):
    q = deque()
    x = n
    q.append((x, 0))
    while q:
        now_x, cnt = q.popleft()
        if now_x < 0 or now_x > 100000 or visited[now_x] == True:
            pass
        if now_x == k:
            break
        q.append((now_x -1, cnt+1))
        visited[now_x-1] = True
        q.append((now_x+1, cnt+1))
        visited[now_x+1] = True
        q.append((2 * now_x, cnt+1))
        visited[now_x*2] = True
        print(q)

    return cnt

print(bfs(n,k))
"""

import sys
from collections import deque

def bfs(v):
    q = deque([v]) #큐 구현을 위해 deque 사용
    while q:
        v = q.popleft()
        print(q)
        if v == k:
            return visited[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)

n, k = map(int, sys.stdin.readline().split())
visited = [0 for i in range(100001)]
print(bfs(n))