from sys import stdin
import copy as dp

n = int(stdin.readline())
t = list(map(int,stdin.readline().split()))
method = list(map(int,stdin.readline().split()))

floor = f =[ en for en in range(n)]

target = [[] for _ in range(3)]
for i,data in enumerate(t):
    target[data].append(i)

def shuffle():
    global floor,n,method
    temp = [0]*n
    for i,data in enumerate(method):
        temp[data]=floor[i]
    floor = dp.deepcopy(temp)

def Compare():
    global target,floor
    for i,data in enumerate(floor):
        i = i % 3
        if data in target[i]:
            pass
        else:
            return False
    return True


cnt = 0
while True:
    rtn = Compare()
    if rtn:
        break
    shuffle()
    cnt +=1
    if floor == f:
        cnt = -1
        break
print(cnt)