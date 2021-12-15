n = int(input())
for _ in range(n):
    stack = []
    data = input()
    success = True
    for d in data:
        if d == '(':
            stack.append(1)
        if d ==')':
            if len(stack) == 0:
                success = False
                break
            else:
                stack.pop()
    if not success or len(stack) != 0:
        print('NO')
    else:
        print('YES')    