data = [1,1,1,2,2]
for _ in range(int(input())):
    n = int(input())
    if n <= len(data):
        print(data[n-1])
    else:
        for i in range(len(data),n):
            data.append(data[i-5] + data[-1])
        print(data[n-1])