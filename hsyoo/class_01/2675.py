n = int(input())
ary = []
for i in range(n):
    tmp = list(input().split())
    a = [case*int(tmp[0]) for case in list(tmp[1])]
    str=a[0]
    for j in range(1, len(a)):
        str += a[j]
    ary.append(str)
for i in ary:
    print(i)
