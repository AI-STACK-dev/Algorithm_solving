from collections import deque
t = int(input())

for _ in range(t):
    flag = 0
    ary = list(input())
    stack = deque([])
    for case in ary:
        if case == '(':
            stack.append(1)
        else:
            if len(stack) == 0:
                print("NO")
                flag = 1
                break
            else:
                stack.pop()
    if flag == 0:
        if len(stack) >0 :
            print("NO")
        else:
            print("YES")