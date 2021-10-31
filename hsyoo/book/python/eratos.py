import math
n = 1000
ary = [True for i in range(n+1)]
ary[0] = False
ary[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if ary[i] == True:
        j = 2
        while i*j <= n:
            ary[i*j] = False
            j+=1
for i in range(2,n+1):
    if ary[i] == True:
        print(i, end = ' ')