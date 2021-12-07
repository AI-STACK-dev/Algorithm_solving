n = int(input())
ans = 0
for i in range(1,n):
    j = i
    i += sum(list(map(int,str(i))))
    if i == n:
        ans = j
        break
print(ans)