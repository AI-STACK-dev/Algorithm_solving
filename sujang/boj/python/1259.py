while True:
    i = input()
    if i == '0':
        break
    if i==i[::-1]:
        print("yes")
    else:
        print("no")