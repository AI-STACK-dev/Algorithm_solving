import sys; input=sys.stdin.readline
data ={}
for s in input().rstrip():
    s = s.upper()
    if not s in data:
        data[s] = 1
    else:
        data[s] += 1
data = sorted(list(data.items()),key=lambda x:x[1])
if len(data)>1 and data[-1][1] == data[-2][1]:
    print('?')
else:
    print(data[-1][0])