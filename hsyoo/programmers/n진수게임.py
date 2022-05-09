def div_n(num, n):
    encode = {'10' : 'A', '11' : 'B', '12' : 'C', '13' : 'D', '14' : 'E', '15' : 'F'}
    list_ = []
    while num != 0:
        res = num % n
        num = num // n
        if 10 <= res <= 15:
            res = encode[str(res)]
        list_.append(str(res))

    return ''.join(reversed(list_))

def solution(n, t, m, p):
    answer = ''
    
    result = '0'
    for i in range(1, m*t+p):
        result += div_n(i, n)
    
    for k in range(p, t*m+p, m):
        if len(answer) == t:
            break
        else:
            answer += result[k-1]
            
    return answer
    

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2,1))
print(solution(16, 16, 2,2))