# ATM 문제
def solve(n,data):
    data.sort()
    Sum = 0
    for _ in range(n):
        Sum += sum(data)
        data.pop()
    return Sum
n = int(input())
data = list(map(int,input().split()))
print(solve(n,data))