def solution(n):
    answer = ''
    while n >= 3:
        res = n % 3
        n = n // 3
        if res == 1 or res == 2:
            answer += str(res)
        else:
            answer += '4'
    if n == 1 or n == 2:
        answer += str(n)
    else:
        answer += '4'
    
    return ''.join(reversed(list(answer)))

print(solution(8))