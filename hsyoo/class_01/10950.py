n = int(input())
ary = []
for i in range(n):
    a,b = map(int, input().split())
    ary.append(a+b)
for case in ary:
    print(case)