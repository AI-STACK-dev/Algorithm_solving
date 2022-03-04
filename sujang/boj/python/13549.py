from collections import deque
n,k = map(int,input().split())
MAX = 100000
visited = [-1]*(MAX+1)

q = deque([n])
visited[n] = 0
while q:
    x = q.popleft()
    if x*2 <= MAX and visited[x*2] == -1:
        q.appendleft(x*2)
        visited[x*2] = visited[x]
    if x+1 <= MAX and visited[x+1] == -1:
        q.append(x+1)
        visited[x+1] = visited[x] + 1
    if x-1 >= 0 and visited[x-1] == -1:
        q.append(x-1)
        visited[x-1] = visited[x] + 1

print(visited[k]) 
