from itertools import permutations

def returnResult(ops, temp):
    for o in ops:
        stack = []
        while temp:
            t = temp.pop(0)
            if t == o:
                a = stack.pop()
                b = temp.pop(0)
                stack.append(str(eval(a+t+b)))
            else:
                stack.append(t)
        temp = stack
    print(temp)
    return abs(int(temp[0]))
        

def solution(ex):
    # exrpession
    prev = ""
    temp = []
    for c in ex:
        if c.isdigit():
            prev += c
        else:
            temp.append(prev)
            temp.append(c)
            prev = ""
    temp.append(prev)

    # operation
    opList = ["+", "*", "-"]
    pm = list(permutations(opList,3))
    ans = 0
    while pm:
        l = pm.pop()
        ans = max(ans, returnResult(l, temp.copy()))
    return ans
print(solution("100-200*300-500+20"))