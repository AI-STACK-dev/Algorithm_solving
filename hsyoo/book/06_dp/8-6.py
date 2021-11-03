n = int(input())

ary = list(map(int, input().split()))
d = [0] * 100

d[0] = ary[0]
d[1] = max(ary[0], ary[1])
for i in range(2,n):
    d[i] = max(d[i-1], d[i-2] + ary[i])
print(d[n-1])