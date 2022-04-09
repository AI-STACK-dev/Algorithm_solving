def solution(N, number):
    dp = []
    for i in range(1,9):
        temp = set()
        temp.add(int(str(N)*i))
        for j in range(1,i):
            for x in dp[j-1]:
                for y in dp[i-j-1]:
                    temp.add(x+y)
                    temp.add(x-y)
                    temp.add(x*y)
                    if y != 0:
                        temp.add(x//y)  

        dp.append(temp)
        if number in temp:
            return i

    return -1