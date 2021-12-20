n = int(input())
data = []
for i in range(n):
    age,name = input().split()
    data.append([i,int(age),name])
data = sorted(data,key=lambda x: (x[1],x[0]))
for i in range(n):
    print(*data[i][1:])