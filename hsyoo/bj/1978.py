import math
n_max = 1000
ary = [True for i in range(n_max+1)]
ary[0] = False
ary[1] = False
for i in range(2, int(math.sqrt(n_max))+1):
    if ary[i] == True:
        j = 2
        while i*j < n_max+1:
            ary[i*j] = False
            j+=1

n = int(input())
input_ = list(map(int, input().split()))
cnt = 0
for case in input_:
    if ary[case] == True:
        cnt +=1
print(cnt)