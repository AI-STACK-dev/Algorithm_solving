N = 10000

check = [True]*(N+1)
ans = []
for i in range(1,N+1):
    if check[i]:
        ans.append(i)
    for j in list(map(int,list(str(i)))):
        i += j
    if i <= N:
        check[i] = False

print(*ans,sep='\n')