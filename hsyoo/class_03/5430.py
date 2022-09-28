from collections import deque

T = int(input())
for t in range(T):
    cmds = input()
    n = int(input())
    # ary = list(map(int, input().strip('[]').split(',')))
    ary = input()
    if len(ary) == 2:
        ary = []
    else:
        ary = list(map(int, ary.strip('[]').split(',')))
    q = deque(ary)
    r_flag = False
    cont_flag = False

    for cmd in cmds:
        if n == 0 and cmd == 'D':
            print('error')
            cont_flag = True
            break
        if r_flag == False and cmd == 'D':
            q.popleft()
            n -= 1
        elif r_flag == True and cmd == 'D':
            q.pop()
            n -= 1
        elif cmd == 'R':
            r_flag = True if r_flag == False else False
    if cont_flag == True:
        continue
    answer = list(q)
    if r_flag == True:
        answer.reverse()
    answer = map(str, answer)
    answer = '[' + ','.join(answer) + ']'
    print(answer)