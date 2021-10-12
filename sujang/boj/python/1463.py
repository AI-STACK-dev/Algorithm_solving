from sys import stdin

n = int(stdin.readline())
data = [0]*(n+1)
# bottom-up으로 다 저장하며 만들자

for i in range(2,n+1):
    data[i] = data[i-1]+1
    if i % 2==0 and data[i] > data[i//2] + 1:
        data[i] = data[i//2] + 1
    if i % 3==0 and data[i] > data[i//3] + 1:
        data[i] = data[i//3] + 1
print(data[-1])
    