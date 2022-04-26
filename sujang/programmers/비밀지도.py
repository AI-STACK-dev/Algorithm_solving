def solution(n, arr1, arr2):
    ans = [ [" "]*n for _ in range(n)]
    for arr in [arr1, arr2]:
        for i in range(n):
            temp = bin(arr[i])[2:].zfill(n)
            for j in range(n):
                if temp[j] != "0" or ans[i][j] != "#":
                    ans[i][j] = "#" if temp[j] == "1" else " "
    answer = []
    for a in ans:
        answer.append("".join(a))
    return answer