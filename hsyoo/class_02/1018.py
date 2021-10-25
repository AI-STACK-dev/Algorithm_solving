n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(input()))

result = []
range_y = n - 7
range_x = m - 7
case = ['B', 'W']
for y in range(range_y):
    for x in range(range_x):
        temp = []
        for i in range(8):
            temp.append(graph[y+i][x:x+8])
        if temp[0][0] == 'W':
            flag = 1
        else:
            flag = 0
        cnt_w = 0
        cnt_b = 0
        for i in range(8):
            for j in range(8):
                if (i+j) % 2 == 0:
                    if temp[i][j] != 'W':
                        cnt_w += 1
                    if temp[i][j] != 'B':
                        cnt_b += 1
                else:
                    if temp[i][j] != 'B':
                        cnt_w += 1
                    if temp[i][j] != 'W':
                        cnt_b += 1
        result.append(cnt_w)
        result.append(cnt_b)
print(min(result))