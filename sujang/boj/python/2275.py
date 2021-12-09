tc = int(input())
for _ in range(tc):
    data = [int(input()) for _ in range(2)]
    table = [[0]*(data[1]+1) for _ in range(data[0]+1)]
    for i in range(1,data[1]+1):
        table[0][i] = i
    for i in range(1,data[0]+1):
        for j in range(1,data[1]+1):
            table[i][j] = sum(table[i-1][:j+1])
    print(table[data[0]][data[1]])