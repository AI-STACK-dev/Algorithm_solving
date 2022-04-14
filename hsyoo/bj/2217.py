n = int(input())
length = n
ary = []
for _ in range(n):
    ary.append(int(input()))

ary.sort()
result = []
for i in range(n):
    result.append(ary[i] * length)
    length -= 1
print(max(result))