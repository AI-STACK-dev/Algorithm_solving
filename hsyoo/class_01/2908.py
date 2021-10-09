a, b = input().split()
a, b = list(a), list(b)
a.reverse()
b.reverse()
tmp_a = a[0]+a[1]+a[2]
tmp_b = b[0]+b[1]+b[2]
print(max(int(tmp_a), int(tmp_b)))