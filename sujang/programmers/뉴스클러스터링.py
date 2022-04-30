def makeSubSet(string):
    n = len(string)
    temp = []
    for i in range(n-1):
        tempStr = string[i:i+2]
        if tempStr.isalpha():
            tempStr = tempStr.lower()
            temp.append(tempStr)
    return temp

def intersection(a, b):
    b = b.copy()
    temp = []
    for x in a:
        if x in b:
            b.remove(x)
            temp.append(x)
    return temp

def union(a, b, c):
    a = a.copy()
    for i in c:
        if i in a:
            a.remove(i)
    return a+b
        
def solution(str1, str2):
    str1List, str2List = makeSubSet(str1), makeSubSet(str2)
    n = intersection(str1List, str2List)
    N = union(str1List, str2List, n)
    if len(N) == 0:
        ans = 1
    else:
        ans = len(n)/len(N)
    return int(ans * 65536)
