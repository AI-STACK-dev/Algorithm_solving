from collections import deque

def check_balance(string_):
    cnt_1 = 0
    cnt_2 = 0
    temp = list(string_)
    for case in temp:
        if case == '(':
            cnt_1 += 1
        else:
            cnt_2 += 1
    if cnt_1 == cnt_2:
        return True
    else:
        return False
def check_correct(string_):
    if check_balance(string_) == False:
        return False
    queue = deque([])
    temp = list(string_)
    for case in temp:
        if case == '(':
            queue.append(case)
        else:
            if len(queue) == 0:
                return False
            else:
                queue.popleft()
    return True

def solution(w):
    print(f"w : {w}")
    temp = ""
    if len(w) == 0:
        return temp
    if check_correct(w):
        return w
    for i in range(2, len(w)+1):
        u, v = w[:i], w[i:]
        if check_balance(u) and check_balance(v):
            break
    if check_correct(u):
        temp = u+solution(v)
        print(f"temp : {temp}")
    else:
        temp = "("
        temp = temp+solution(v)+")"
        u_temp = list(u)[1:-1]
        for i in range(len(u_temp)):
            if u_temp[i] == '(':
                u_temp[i] = ')'
            else:
                u_temp[i] = '('
        temp = temp + "".join(u_temp)
        print(f"temp : {temp}")
    return temp
