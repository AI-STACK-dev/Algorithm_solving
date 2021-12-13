import sys; input = sys.stdin.readline;

DP0 = [0] * 41
DP1= [0] * 41
DP0[0] = 1
DP1[1] = 1
for i in range(2,41):
    DP0[i] = DP0[i - 1] + DP0[i - 2]
    DP1[i] = DP1[i - 1] + DP1[i - 2]

t = int(input())
for _ in range(t):
    n = int(input())
    print(DP0[n], DP1[n])

# def fibonacci(n):
#     global cnt0
#     global cnt1
#     if n == 0:
#         cnt0 += 1
#         return 0
#     elif n == 1:
#         cnt1 += 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
