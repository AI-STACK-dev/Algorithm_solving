import math

def is_prime(n):
    flag = 1
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            flag = 0
    if flag == 1:
        return True
    else:
        return False

def make_k(n, k):
    s = ''
    while n != 0:
        res = n % k 
        s += str(res)
        n = n // k
    temp = ''
    for i in range(len(s)-1, -1, -1):
        temp += s[i]
    return temp

def solution(n, k):
    answer = -1
    k_s = make_k(n, k)
    
    temp = ''
    list_ = []
    for idx, case in enumerate(k_s):
        if int(case) > 0:
            temp += case
        else:
            if len(temp) > 0:
                list_.append(int(temp))
                temp = ''
            else:
                continue
    if len(temp) > 0:
        list_.append(int(temp))

    cnt = 0
    for digit_ in list_:
        if digit_ == 1:
            continue
        elif is_prime(digit_):
            cnt +=1
    return cnt

print(solution(437674, 3))
print(solution(110011, 10))