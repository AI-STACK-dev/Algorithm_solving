def check_balance(w):
    cnt_1 = 0
    cnt_2 = 0
    for case in w:
        if case == '(':
            cnt_1 += 1
        else:
            cnt_2 += 1
    if cnt_1 == cnt_2:
        return True
    else:
        return False
def check_correct(w):
    if check_balance(w) == False:
        return False
    else:
        stack = []
        for case in w:
            if case == '(':
                stack.append('(')
            elif len(stack) == 0 and case == ')':
                return False
            elif len(stack) > 0 and case == ')':
                stack.pop()
        return True

def solution(p):
    if len(p) == 0:
        return ''
    if check_correct(p):
        return p

    n = len(p)
    stack = [p[0]]
    for idx in range(2,n+1):
        u,v = p[:idx], p[idx:]
        if check_balance(u) == True or check_correct(u) == True:
            break
    
    if check_correct(u) == True:
        return u + solution(v)
    else:
        temp = '(' + solution(v) + ')'
        u = u[1:-1]
        u_t = ''
        for case in u:
            if case == '(':
                u_t += ')'
            else:
                u_t += '('
        return temp + u_t

    # return answer

print(solution("(()())()"	))
print(solution(')('))
print(solution("()))((()"	))
