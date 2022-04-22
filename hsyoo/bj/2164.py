from collections import deque
n = int(input())
ary = [i for i in range(1,n+1)]
q = deque(ary)
for _ in range(n):
    num = q.popleft()
    if len(q) == 0:
        break
    num = q.popleft()
    q.append(num)
print(num)