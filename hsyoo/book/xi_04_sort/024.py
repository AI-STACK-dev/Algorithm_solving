n = int(input())
ary = list(map(int, input().split()))
ary.sort()
print(ary[(n-1)//2])