from collections import deque
n,k = map(int,input().split())
data = list(range(1,n+1))

q = deque(data)
ans = []
while q:
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())
print("<",end='')
print(*ans, sep=', ',end='')
print(">")