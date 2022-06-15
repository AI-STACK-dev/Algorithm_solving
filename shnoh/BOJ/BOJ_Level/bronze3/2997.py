import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
data.sort()
dif1 = data[1] - data[0]
dif2 = data[2] - data[1]
if dif1 == dif2:
    print(data[2] + dif1)
elif dif1 > dif2:
    print(data[0] + dif2)
else:
    print(data[1] + dif1)