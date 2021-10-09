n = int(input())
sol = []
for i in range(n):
    ary = list(input())
    sum = 0
    cnt = 0
    for case in ary:
        if case == 'O':
            cnt+=1
            sum +=cnt
        else:
            cnt = 0
    sol.append(sum)
for sol_ in sol:
    print(sol_)

