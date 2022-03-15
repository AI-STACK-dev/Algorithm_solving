from collections import deque
a,b = map(int,input().split())
ans = int(1e9)
q = deque([(a,0)])
while q:
    x,cnt = q.popleft()
    if x>b:
        continue
    if x == b:
        ans = min(ans,cnt)
        continue
    q.append((x*2,cnt+1))
    q.append((x*10+1,cnt+1))
print(ans+1 if ans < int(1e9) else -1)
