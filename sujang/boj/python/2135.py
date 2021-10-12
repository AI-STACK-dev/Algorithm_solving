from sys import stdin

data = stdin.readline()[:-1]
length = len(data)
matrix = [[None]*length for _ in range(length)]

def check(start,d,size):
    global data
    temp = []
    for i in range(start,start+size+1,d):
        temp.append(data[i:i+d])
    return all_same(temp)

def all_same(items):
    return all(x == items[0] for x in items)

# matrix[i][j]에서 i==j인 경우 1로 초기화
for i in range(length):
    matrix[i][i] = 1

for size in range(1, length):
    div = []
    for i in range(1,size+1):
        if (size+1) % i ==0:
            div.append(i)
    
    for start in range(0,length-size):
        ans = size+1
        for d in div:
            if check(start,d,size):
                ans = min(ans, matrix[start][start+d-1] + 2 + len(str((size+1)//d)))
        for j in range(0,size):
            ans = min(ans, matrix[start][start+j]+matrix[start+j+1][start+size])
        matrix[start][start+size] = ans
print(matrix[0][length-1])



