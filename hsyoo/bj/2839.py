n = int(input())
result = 0
while n >= 3:
    # print(n)
    if n % 5 == 0:
        r = n // 5
        result += r
        n = 0 
    else:
        n -= 3
        result += 1

if n != 0:
    print(-1)
else:
    print(result)
