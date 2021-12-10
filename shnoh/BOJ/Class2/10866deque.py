import sys; input = sys.stdin.readline;
from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    instruction = input().rstrip().split()
    if instruction[0] == 'push_front':
       queue.appendleft(int(instruction[1]))
    elif instruction[0] == 'push_back':
       queue.append(int(instruction[1]))
    elif instruction[0] == 'pop_front':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif instruction[0] == 'pop_back':
        if queue:
            print(queue.pop())
        else:
            print(-1)
    elif instruction[0] == 'size':
        print(len(queue))
    elif instruction[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif instruction[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)