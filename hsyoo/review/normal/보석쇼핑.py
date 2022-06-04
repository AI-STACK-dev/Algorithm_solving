from collections import defaultdict

def solution(gems):
    n = len(gems)
    unique = set(gems)
    check_len = len(unique)
    counter = defaultdict(int)
    start, end = 0, 0
    min_ = int(1e9)

    while end < n:
        counter[gems[end]] += 1
        end += 1
        if len(counter) == check_len:
            while start < end:
                if counter[gems[start]] > 1:
                    counter[gems[start]] -= 1
                    start += 1
                elif end - start < min_:
                    min_ = end - start
                    answer = [start+1, end]
                    break
                else:
                    break
    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["AA", "AB", "AC", "AA", "AC"]))
print(solution(["XYZ", "XYZ", "XYZ"]))
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
