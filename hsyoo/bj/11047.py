n, k =map(int, input().split())
ary = []
for _ in range(n):
    ary.append(int(input()))
ary.reverse()
result = 0
for case in ary:
    if k == 0:
        break
    elif k < case:
        continue
    else:
        div = k // case
        r = k % case
        result += div
        k = r
print(result)