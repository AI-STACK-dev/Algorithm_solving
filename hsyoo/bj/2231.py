n = int(input())
flag = 0
ans = 0
for i in range(1, n):
    temp = list(map(int, list(str(i))))
    sum_ = sum(temp)
    if i + sum_ == n:
        flag = 1
        ans = i
        break
    

if flag == 0:
    print(0)
else:
    print(ans)
