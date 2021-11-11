import sys
def check(n):
    cnt = 0
    while n >= 3:
        if n == 3: 
            return cnt + 1
        elif n % 5 == 0:
            return cnt + n // 5
        else:
            n = n - 3
            cnt += 1
    return -1
    
n = int(sys.stdin.readline())
print(check(n))

# sys.setrecursionlimit(10**6)
# def check(n):
#     if n == 3 or n == 5: 
#         return 1
#     elif n < 5:
#         return 2000
#     else: 
#         return min(check(n-5), check(n-3)) + 1
    
# n = int(sys.stdin.readline())
# k = check(n)
# if k < 2000:
#     print(k)
# else:
#     print(-1)
