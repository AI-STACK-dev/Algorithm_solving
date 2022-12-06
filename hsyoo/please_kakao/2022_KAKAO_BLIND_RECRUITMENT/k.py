import math

def calc_k(n, k):
    string = ''
    while n != 0:
        mod = n % k
        n = n // k
        string += str(mod)
    string = string[::-1]
    return string


def is_prime(num):
    if len(num) == 0:
        return False
    num = int(num)
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    string = calc_k(n, k)
    cands = list(string.split('0'))
    
    for cand in cands:
        if is_prime(cand):
            answer += 1
    return answer

print(solution(437674, 3))
print(solution(110011, 10))