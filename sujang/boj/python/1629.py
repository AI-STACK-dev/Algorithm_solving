a,b,c = map(int,input().split())

def dAndQ(a,b):
    if b == 1:
        return a % c
    
    temp = dAndQ(a, b//2)

    if b % 2 == 0:
        return temp*temp % c
    else: 
        return temp*temp*a % c

print(dAndQ(a,b))