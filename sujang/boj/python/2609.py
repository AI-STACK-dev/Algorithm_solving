def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    return a
a,b = map(int,input().split())
r = gcd(a,b)
print(r)
print((a*b)//r)