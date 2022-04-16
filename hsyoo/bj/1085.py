x,y,w,h = map(int, input().split())
print(min(min(h-y, y), min(w-x, x)))