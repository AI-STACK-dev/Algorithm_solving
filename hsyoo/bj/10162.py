t = int(input())
#300, 60, 10
result = [0] * 3
while t >= 10:
    if t >= 300:
        div = t // 300
        t = t % 300
        result[0] = div
    elif t >= 60:
        div = t // 60
        t = t % 60
        result[1] = div
    elif t >= 10:
        div = t//10
        t = t%10
        result[2] = div
if t != 0:
    print(-1)
else:
    for case in result:
        print(case, end=' ')
    print()