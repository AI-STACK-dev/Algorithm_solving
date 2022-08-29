import sys; input = sys.stdin.readline;
n = int(input())
res = abs(5 - n)
if res <= 1:
    print(3)
elif res <=3:
    print(2)
else:
    print(1)