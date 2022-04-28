def solution(record):
    repoDict = {}
    for r in record:
        temp = r.split()
        if temp[0] == "Enter" or  temp[0] == "Change":
            repoDict[temp[1]] = temp[2]
    
    result = []
    for r in record:
        temp = r.split()
        if temp[0] == "Enter":
            result.append(repoDict[temp[1]] + "님이 들어왔습니다.")
        elif temp[0] == "Leave":
            result.append(repoDict[temp[1]] + "님이 나갔습니다.")
    
    return result