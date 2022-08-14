while True:
    s = input()
    if s == "***":
        break
    # n = len(s)
    # for i in range(n - 1, -1, -1):
    #     print(s[i], end = '')
    # print('')
    # n = len(s)
    # data = []
    # for i in range(n - 1, -1, -1):
    #     data.append(s[i])
    # print("".join(data))
    print(s[::-1])