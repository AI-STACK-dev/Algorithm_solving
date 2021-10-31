import math

m, n = map(int, input().split())
n_max = 1000000
ary = [True for i in range(n_max+1)]
ary[0] = False
ary[1] = False
for i in range(2,int(math.sqrt(n_max))+1):
    if ary[i] == True:
        j = 2
        while i*j <= n_max:
            ary[i*j] = False
            j+=1
for i in range(m, n+1):
    if ary[i] == True:
        print(i)