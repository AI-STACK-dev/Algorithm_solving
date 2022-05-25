import math

# def solution(arr):
#     answer = 1
#     for case in arr:
#         answer = math.lcm(answer, case)
#     return answer

def gcd(a,b):
    while b>0:
        a,b = b, a%b
    return a
def lcm(a,b):
    return a*b / gcd(a,b)

def solution(arr):
    answer = 1
    for case in arr:
        answer = lcm(answer, case)
    return int(answer)

print(solution([2,6,8,14]))