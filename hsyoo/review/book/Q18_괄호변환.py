from collections import deque

def is_balance(s):
    cnt_left = 0
    cnt_right = 0
    for case in s:
        if case == '(':
            cnt_left +=1
        elif case == ')':
            cnt_right +=1
    if cnt_left == cnt_right:
        return True
    else:
        return False

def is_correct(s):
    if is_balance(s) != True:
        return False
    
    queue = deque([])
    for case in s:
        if case == '(':
            queue.append('(')
        else:
            if len(queue) == 0:
                return False
            elif len(queue) > 0:
                queue.pop()
    if len(queue) > 0:
        return False
    return True

def change(s):
    result = ''
    for case in s:
        if case == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(s):
    if len(s) == 0:
        return ''
    if is_correct(s):
        return s
    
    for i in range(1, len(s)+1):
        u, v = s[:i],s[i:] 
        if is_balance(u) and is_balance(v):
            break
    if is_correct(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + change(u[1:-1])

print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))