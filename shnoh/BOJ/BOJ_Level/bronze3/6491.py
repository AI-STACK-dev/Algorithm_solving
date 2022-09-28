import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
for n in data:
    if n == 0:
        break
    A = []
    for i in range(1, n):
        if n % i == 0:
            if i not in A:
                A.append(i)
            x = n // i
            if x != n and x not in A:
                A.append(x)
    Sum = sum(A)
    if Sum == n:
        print(f'{n} PERFECT')
    elif Sum > n:
        print(f'{n} ABUNDANT')
    else:
        print(f'{n} DEFICIENT')