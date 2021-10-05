n = int(input())
ary = list(map(int, input().split()))
max_ = max(ary)
print(((sum(ary))/max_*100)/n)