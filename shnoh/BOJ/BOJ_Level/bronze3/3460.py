import sys; input = sys.stdin.readline;
t = int(input())
data = [ int(input()) for _ in range(t)]
for num in data:
    k = 0
    while num > 0:
        if num % 2 == 1:
            print(k, end=' ')
        num = num // 2
        k += 1
    print()