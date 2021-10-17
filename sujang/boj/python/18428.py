from sys import stdin
from itertools import combinations

n = int(stdin.readline().rstrip())
# data = [stdin.readline().rstrip().split() for _ in range(n)]
data = []
teachers = []
voids = []
for i in range(n):
    data.append(stdin.readline().rstrip().split())
    for j,element in enumerate(data[i]):
        if element =='X':
            voids.append([i,j])
        if element =='T':
            teachers.append([i,j])

def find(x,y,i):
    global n
    if i == 0:
        while y<n:
            
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y += 1
    if i == 1:
        while y>=0:
           
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            y -= 1
    if i == 2:
        while x>=0:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x -= 1
    if i == 3:
        while x < n:
            if data[x][y] == 'S':
                return True
            if data[x][y] == 'O':
                return False
            x += 1
    return False

def test():
    for x,y in teachers:
        for i in range(4):
            if find(x,y,i):
                return False
    return True
pos = list(combinations(voids,3))
ans = False
for p in pos:
    for x,y in p:
        data[x][y] = 'O'
    if test():
        ans = True
        break
    for x,y in p:
        data[x][y] = 'X'

if ans:
    print('YES')
else:
    print('NO')
