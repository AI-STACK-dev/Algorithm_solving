from collections import defaultdict

def solution(survey, choices):
    answer = ''
    db = defaultdict(int)
    check1 = ['R', 'C', 'J', 'A']
    check2 = ['T', 'F', 'M', 'N']
    for query, choice in zip(survey, choices):
        a, b = query[0], query[1]
        if choice - 4 > 0:
            db[b] += abs(choice - 4)
        else:
            db[a] += abs(choice - 4)
    for i in range(4):
        a, b = check1[i], check2[i]
        if db[a] < db[b]:
            answer += b
        else:
            answer += a

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]	))
print(solution(["TR", "RT", "TR"]	, [7, 1, 3]	))