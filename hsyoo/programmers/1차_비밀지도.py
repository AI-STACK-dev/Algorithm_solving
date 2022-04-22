def bit_2(x, n):
    temp = []
    while x != 0:
        div = x//2
        res = x%2
        temp.append(res)
        x = div

    if len(temp) > n:
        temp = temp[1:]
    elif len(temp) < n:
        for i in range(n - len(temp)):
            temp.append(0)
    temp.reverse()
    return temp

def solution(n, arr1, arr2):
    ary1, ary2 = [],[]
    for i in range(n):
        ary1.append(bit_2(arr1[i],n))
        ary2.append(bit_2(arr2[i],n))
    print(ary1, ary2)
    result = []
    for i in range(n):
        s = ''
        for j in range(n):
            if ary1[i][j] == 0 and ary2[i][j] == 0:
                s+=' '
            else:
                s+='#'
        result.append(s)
    print(s)
    return result