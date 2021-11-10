n = int(input())
d = [0] * (5001)

d[1] = 1
d[2] = 1
d[3] = 1
d[4] = 1
d[5] = 1
for i in range(6,5001):
    if i%2 == 0 and d[i//2] == 1:
        d[i] = 1
    if i%3 == 0 and d[i//3] == 1:
        d[i] = 1
    if i % 3 == 0 and d[i//5] == 1:
        d[i] = 1

cnt = 0
for i in range(5001):
    if d[i] == 1:
        cnt +=1
    if cnt == n:
        print(i)
        break
