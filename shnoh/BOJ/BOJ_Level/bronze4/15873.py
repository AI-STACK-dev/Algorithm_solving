import sys; input = sys.stdin.readline;
data = input().rstrip()
n = len(data)
res = 0
if n == 2:
    res = int(data[0]) + int(data[1])
elif n == 3:
    if int(data[1]) == 0:
        res = 10 + int(data[2])
    else:
        res = 10 + int(data[0])
else:
    res = 20
print(res)