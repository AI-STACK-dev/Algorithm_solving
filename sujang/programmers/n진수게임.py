def convertNumber(number, notation):
    temp = ""
    if number == 0:
        return "0"
    while number > 0:
        number, remain = divmod(number, notation)
        if remain >= 10:
            remain = chr(ord("A") + remain - 10)
        temp += str(remain)
    return temp[::-1]
    
def solution(n, t, m, p):
    repo = ""
    target = t*m 
    cnt = i = 0
    while cnt < target:
        temp = convertNumber(i, n)
        repo += temp
        i += 1
        cnt += len(temp)
    
    ans = ""
    for i in range(t):
        ans += repo[(i*m)+(p-1)]
    return ans 