n = int(input())
token = '666'
ary = [0]
# 1sec : 2000만, 20,000,000 int(1e8)
for i in range(1, int(1e8)):
    if token in str(i):
        ary.append(i)
print(ary[n])