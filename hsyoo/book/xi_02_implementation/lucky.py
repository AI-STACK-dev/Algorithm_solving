n = int(input())
ary_ = list(str(n))
length = len(ary_)//2
left = n // (10**length)
right = n % (10**length)
left = sum(list(map(int, list(str(left)))))
right = sum(list(map(int, list(str(right)))))
if left == right:
    print("LUCKY")
else:
    print("READY")