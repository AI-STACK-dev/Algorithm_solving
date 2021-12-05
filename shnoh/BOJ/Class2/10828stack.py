import sys; input = sys.stdin.readline;

n = int(input())
stack = []
for _ in range(n):
    instruction = input().rstrip()
    if instruction[1] == 'u':
       a, b = instruction.split()
       stack.append(int(b))
    elif instruction[0] == 'p':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif instruction[0] == 's':
        print(len(stack))
    elif instruction[0] == 'e':
        if stack:
            print(0)
        else:
            print(1)
    else:
        if stack:
            print(stack[-1])
        else:
            print(-1)