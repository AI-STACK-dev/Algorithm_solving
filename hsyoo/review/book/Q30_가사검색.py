from bisect import bisect_left, bisect_right

def count_range(ary, l_query, r_query):
    # print(ary, l_query, r_query)
    left = bisect_left(ary, l_query)
    right = bisect_right(ary, r_query)
    return right - left

def solution(words, queries):
    answer = []
    word_list = [[] for _ in range(10001)]
    word_list_rev = [[] for _ in range(10001)]
    for word in words:
        length = len(word)
        word_list[length].append(word)
        word_list_rev[length].append(word[::-1])
    for length in range(10001):
        word_list[length].sort()
        word_list_rev[length].sort()

    for query in queries:
        length = len(query)
        # print(word_list[length], query)
        if query[0] != '?':
            answer.append(count_range(word_list[length], query.replace('?', 'a'), query.replace('?', 'z')))
        else:
            answer.append(count_range(word_list_rev[length], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z')))
    
    return answer

print(solution(['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao'], ['fro??', '????o', 'fr???', 'fro???', 'pro?']))