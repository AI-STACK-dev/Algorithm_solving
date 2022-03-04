num = int(input())
div = 2
while num != 1:
    if num % div == 0:
        num //=div
        print(div)
    else:
        div += 1
