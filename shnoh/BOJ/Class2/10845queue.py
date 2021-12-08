import sys; input = sys.stdin.readline;
from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    instruction = input().rstrip()
    if instruction[1] == 'u':
       a, b = instruction.split()
       queue.append(int(b))
    elif instruction[0] == 'p':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif instruction[0] == 's':
        print(len(queue))
    elif instruction[0] == 'e':
        if queue:
            print(0)
        else:
            print(1)
    elif instruction[0] == 'f':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)