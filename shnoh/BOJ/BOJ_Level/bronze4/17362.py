import sys; input = sys.stdin.readline;
n = int(input())
x = (n - 1) % 8
if x == 0:
    res = 1
elif x == 1 or x == 7:
    res = 2
elif x == 2 or x == 6:
    res = 3
elif x == 3 or x == 5:
    res = 4
else:
    res = 5
print(res)