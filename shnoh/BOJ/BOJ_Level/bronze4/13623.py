import sys; input = sys.stdin.readline;
data = list(map(int, input().split()))
alpha = ['A','B','C']
zero_cnt = 0
one_cnt = 0
zero = -1
one = -1

for i in range(3):
    if data[i] == 0:
        zero_cnt += 1
        zero = i
    else:
        one_cnt += 1
        one = i
if zero_cnt == 1:
    print(alpha[zero])
elif one_cnt == 1:
    print(alpha[one])
else:
    print('*')
