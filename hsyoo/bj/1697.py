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
from collections import deque

n, k = map(int, input().split())
visited = [False] * 100001

q = deque()
q.append((n,0))
visited[n] = True
while q:
    now,cnt = q.popleft()
    if now == k:
        break
    for i in [now-1, now+1, 2*now]:
        if 0<=i<=100000 and visited[i] == False:
            q.append((i, cnt + 1))
            visited[i] = True
print(cnt)