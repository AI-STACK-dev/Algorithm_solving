n = int(input())
ary = set(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))
for i in range(m):
    if check[i] in ary:
        print(1)
    else:
        print(0)