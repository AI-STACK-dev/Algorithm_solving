import sys; input = sys.stdin.readline;
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    a = a % 10
    if a == 0:
        print(10)
    else:
        b = b % 4 + 4
        res = (a ** b) % 10
        print(res)
# 1
# 2 4 8 6
# 3 9 7 1
# 4 6
# 5
# 6
# 7 9 3 1
# 8 4 2 6
# 9 1
# 0