'''
문제 2. 
43분 소요
문제를 꼼꼼히 읽자,,,
'''
import math
# 소수 판별 함수
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n%i == 0:
            return False
    return True
        
import re
def solution(n, k):
    # 1. k진수로 변환
    if n < k:
        converted_n = n
    else:
        temp = n
        converted_n = exp = 0
        while (temp >= k):
            quo = temp // k
            rem = temp % k
            converted_n += rem*(10**exp)
            exp += 1
            temp //= k
        converted_n += quo*(10**exp)
    
    # 2. "0"을 이용하여 분할
    cnt = 0
    converted_n = str(converted_n).split("0")
    for i in converted_n:
        if i.isdigit():
            if isPrime(int(i)):
                cnt +=1
    return cnt