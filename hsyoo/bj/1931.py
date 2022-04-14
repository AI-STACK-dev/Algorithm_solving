import sys
input = sys.stdin.readline

n = int(input())
array = []
for _ in range(n):
    a,b = map(int, input().split())
    array.append((a,b))

array = sorted(array, key = lambda x : (x[1], x[0]))

start = array[0][0]
end = array[0][1]
result = 1
for i in range(1, n):
    if array[i][0] >= end:
        result += 1
        end = array[i][1]
print(result)