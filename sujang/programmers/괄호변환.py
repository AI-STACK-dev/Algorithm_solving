def split(p):
    stack = [p[0]]
    i = 1
    while stack:
        if p[i] == stack[-1]:
            stack.append(p[i])
        else:
            stack.pop()
        i+=1
    if i >= len(p):
        return p[:i],''
    return p[:i],p[i:]

def check(p):
    cnt = 0
    for ch in p:
        if ch =='(':
            cnt += 1
        elif cnt > 0:
            cnt -= 1
    return cnt ==0

            
def rev(u):
    rtn = ''
    for ch in u:
        if ch =='(':
            rtn += ')'
        else:
            rtn += '('
    return rtn
    
def solution(p):
    if p =='':
        return ''
    u,v = split(p)
    if check(u):
        return u+solution(v)
    else:
        empty = '('
        empty += solution(v)
        empty += ')'
        empty += rev(u[1:-1])
        return empty
