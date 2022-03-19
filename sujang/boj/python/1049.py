n,m = map(int,input().split())
data = [ list(map(int,input().split())) for _ in range(m)]
a = sorted(data,key=lambda x:x[0])[0][0]
b = sorted(data,key=lambda x:x[1])[0][1]
div = n//6
quo = n%6
print(min([a*(div+1), (a*div)+(quo*b) ,b*n]))
