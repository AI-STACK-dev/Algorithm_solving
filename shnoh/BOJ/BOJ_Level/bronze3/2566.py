import sys; input = sys.stdin.readline;
data = []
Max = 0
for i in range(9):
    data.append(list(map(int, input().split())))
for i in range(9):
    for j in range(9):
        if data[i][j] > Max:
            row = i
            col = j
            Max = data[i][j]
print(Max)
print(row + 1, col + 1)