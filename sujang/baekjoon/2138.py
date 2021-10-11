import copy
def on(arr,idx):
    arr[idx] = 1- arr[idx]
    if idx == 0:
        arr[idx+1] = 1- arr[idx+1]
    elif idx == len(arr)-1:
        arr[idx-1] = 1- arr[idx-1]  
    else:
        arr[idx-1] = 1- arr[idx-1] 
        arr[idx+1] = 1- arr[idx+1] 
    return arr
def solve(n,a,b):
    fon = copy.deepcopy(a)
    fof = copy.deepcopy(a)
    fon = on(fon,0)

    onc = 1
    ofc = 0
    for i in range(1,n):
        if fon[i-1] != b[i-1]:
            fon = on(fon,i)
            onc += 1
        if fof[i-1] != b[i-1]:
            fof = on(fof,i)
            ofc += 1

    result = []
    if fon == b:
        result.append(onc)
    if fof == b:
        result.append(ofc)
    
    if len(result) == 0:
        return -1
    else:
        return min(result)


n = int(input())
a = [int(x) for x in input()]
b = [int(x) for x in input()]
print(solve(n,a,b))