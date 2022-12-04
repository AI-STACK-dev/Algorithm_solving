while True:
    try:
        s = input()
        if s == "":
            break
        a,b,c = map(int, s.split())
        print(max(b - a, c - b) - 1)
    except:
        break