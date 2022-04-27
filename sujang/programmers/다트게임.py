def solution(d):
    prev = ""
    awardDict = {"*":2, "#":-1}
    ans = []
    for i in range(len(d)):
        c = d[i]
        if c.isdigit():
            prev += c
        elif c in ["S", "D", "T"]:
            if c == "S":
                ans.append(int(prev))
            elif c == "D":
                ans.append(int(prev)**2)
            elif c == "T":
                ans.append(int(prev)**3)
            prev = ""
        else:
            if len(ans) >= 2 and c == "*":
                ans[-2] *= awardDict[c]
            ans[-1] *= awardDict[c]
    print(ans)
    return sum(ans)

d = "1D2S#10S"
print(solution(d))