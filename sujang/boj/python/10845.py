from collections import deque
import sys; input = sys.stdin.readline
n = int(input().rstrip())
d = deque([])
for _ in range(n):
    cmd = input().rstrip().split()
    if cmd[0] == 'push':
        d.append(int(cmd[1]))
    elif cmd[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if d:
            print(d[-1])
        else:
            print(-1)       
    elif cmd[0] == 'size':
        print(len(d))
    elif cmd[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    else:
        if d:
            print(d.popleft())
        else:
            print(-1)