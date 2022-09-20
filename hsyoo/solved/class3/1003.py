# T = int(input())
# # dp = [0] * 41

# def fibo(n):
#     global dp
#     dp[n] += 1
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n-1) + fibo(n-2)
# for _ in range(T):
#     dp = [0] * 41
#     n = int(input())
#     fibo(n)
#     print(dp[0], dp[1])

"""
시간 초과
"""

zeros = [1, 0, 1]
ones = [0, 1, 1]

def fibo(n):
    length = len(zeros)
    if n >= length:
        for i in range(length, n + 1):
            zeros.append(zeros[i-1] + zeros[i-2])
            ones.append(ones[i-1] + ones[i-2])
    print(zeros[n], ones[n])

T = int(input())
for _ in range(T):
    fibo(int(input()))



    
