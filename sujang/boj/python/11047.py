# 동전 0문제
def solve(n,k,data):
    count = 0
    for coin in reversed(data):
        if k >= coin:
            count += k//coin
            k = k%coin
    return count
n,k = map(int,input().split())
data = [int(input()) for _ in range(n)]
print(solve(n,k,data))