n = int(input())
roads = list(map(int,input().split()))
prices = list(map(int,input().split()))

ans = 0
minPrice = int(1e9)
for i in range(len(roads)):
    minPrice = min(minPrice, prices[i])
    ans += minPrice*roads[i]
print(ans)
