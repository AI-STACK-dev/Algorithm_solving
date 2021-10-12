# 회의실 배정 문제
def solve(n,data):
    data = sorted(data, key = lambda x: (x[1],x[0]))
    count = 1
    end = data[0][1]
    for i in data[1:]:
        if i[0] >= end:
            count += 1
            end = i[1]
    return count
n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
print(solve(n,data))