n,x=map(int,input().split())
print( *[ i for i in list(map(int,input().split())) if i<x ] )