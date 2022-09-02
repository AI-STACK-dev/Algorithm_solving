import sys; input = sys.stdin.readline;
while True:
    n = int(input())
    if n == 0:
        break
    while n >= 10:
        Droot = 0
        while n >= 10:
            Droot += n % 10
            n = n // 10
        Droot += n
        n = Droot
    print(n)