import sys; input = sys.stdin.readline;
t = int(input())
for _ in range(t):
    n = int(input())
    s1 = s2 = s3 = 0
    for i in range(1, n + 1):
        s1 += i
    for i in range(1, 2 * n + 1):
        if i % 2:
            s2 += i
        else:
            s3 += i
    print(s1, s2, s3)