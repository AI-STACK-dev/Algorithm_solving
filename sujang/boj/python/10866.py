from collections import deque
import sys;input = sys.stdin.readline

n = int(input())
d = deque([])
for _ in range(n):
    cmd = input().split()
    if cmd[0] == 'push_front':
        d.appendleft(int(cmd[1]))
    elif cmd[0] == 'push_back':
        d.append(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if d:
            num = d.popleft()
            print(num)
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if d:
            num = d.pop()
            print(num)
        else:
            print(-1)  
    elif cmd[0] == 'size':
        print(len(d))
    elif cmd[0] == 'empty':
        if d:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if d:
            print(d[0])
        else:
            print(-1)
    else:
        if d:
            print(d[-1])
        else:
            print(-1)