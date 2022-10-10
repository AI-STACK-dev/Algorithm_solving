import sys; input = sys.stdin.readline;
t1 = int(input())
t2 = int(input())
res = 2
while t2 <= t1:
    res += 1
    temp = t1 - t2
    t1 = t2
    t2 = temp
print(res)