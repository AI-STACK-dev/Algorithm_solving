import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
operaters = list(map(int, sys.stdin.readline().split())) # + - * //
# print((12) // 5)
# 음수의 나눗셈의 경우 고려 필요할 듯?
# 경우의 수를 계산해 보면... 결국 n-1 어떻게 배치하느냐,,,?
#for i in range(n):