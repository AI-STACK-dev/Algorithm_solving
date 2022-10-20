import sys; input = sys.stdin.readline;
t = int(input())
for j in range(t):
    if j != 0:
        print()
    n = int(input())
    res = 0
    for i in range(1, n):
        if n % i == 0:
            res += i
    # res = 1
    # for i in range(2, int(n ** 0.5) + 1):
    #     if n % i == 0:
    #         res += i
    #         x = n // i
    #         if x != i:
    #             res += x
    if res == n:
        print(f"{n} is a perfect number.")
    elif res < n:
        print(f"{n} is a deficient number.")
    else:
        print(f"{n} is a abundant number.")