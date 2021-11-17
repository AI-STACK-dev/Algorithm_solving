#평균은 넘겠지
import sys

C = int(sys.stdin.readline())
for i in range(C):
    temp = list(map(int,sys.stdin.readline().split()))
    mean = (sum(temp) - temp[0]) / temp[0] # 실수 나눗셈
    cnt = 0
    for j in range(1, temp[0] + 1):
        if temp[j] > mean:
            cnt += 1
    print(f'{100 * cnt / temp[0]:.3f}%')