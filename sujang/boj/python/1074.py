n,r,c = map(int,input().split())

def search(n,r,c):
    n -= 1
    m = 2**n

    if m == 1:
        return (2*r) + c
    
    isCol = isRow = False
    if (r-m) >= 0:
        isRow = True
        r -= m
    if (c - m) >= 0:    
        isCol = True
        c -= m

    if isCol^isRow:
        if isCol:
            amt = 1
        else:
            amt = 2
    elif isCol and isRow:
        amt = 3
    else:
        amt = 0
    
    return ((m**2)*amt) + search(n,r,c)

print(search(n,r,c))



