n = int(input())
m = int(input())
if (m > 0):
    data = input().split()
else:
    data = []
ans = abs(n-100)

for num in range(1000001):
    flag = True
    for ch in str(num):
        if ch in data:
            flag = False
            break
    if flag:
        ans = min(ans, len(str(num)) + abs(n-num))
print(ans)
