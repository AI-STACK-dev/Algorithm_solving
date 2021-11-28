import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque([i for i in range(1, n + 1)])
even = True
while queue:
    if even:
        last = queue.popleft()
        even = False
    else:
        last = queue.popleft()
        queue.append(last)
        even = True
print(last)
