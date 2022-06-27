# def binary_search_left(len_words, words, query):
#     n = len(query)
#     start = 0
#     end = len_words
#     prefix = False
#     suffix = False

#     if query[0] == '?':
#         temp = query.split('?')
#         prefix = True
#         s = temp[-1]
#     else:
#         temp = query.split('?')
#         suffix = True
#         s = temp[0]

#     while start <= end:
#         mid = (start + end) // 2
#         if prefix == True and suffix == False:
#             if len(words[mid]) < len(query):
#                 start = mid + 1
#             elif len(words[mid]) > len(query):
#                 end = mid -1
#             else:
                 
    
# def solution(words, queries):
#     words.sort(key = lambda x: len(x))
#     length = len(words)
#     answer = []
#     return answer

"""
GG
"""

import sys
sys.setrecursionlimit(100001)

def make_trie(trie, words):
    for word in words:
        cur = trie
        l = len(word)
        for w in word:
            if w in cur:
                cur = cur[w]
                cur['!'].append(l) #기존에 존재하는 노드라면 단어 하나하나를 dictionary로
            else:
                cur[w] = {}
                cur = cur[w]
                cur['!'] = [l]
    return trie

def search_trie(trie, query, length):
    count = 0
    if query[0] == '?':
        return trie['!'].count(length)
    elif query[0] in trie:
        count += search_trie(trie[query[0]], query[1:], length)

    return count

def solution(words, queries):
    answer = []
    rev_words, counted = [], []
    for w in words:
        rev_words.append(w[::-1])
        counted.append(len(w))
    
    trie = make_trie({}, words)
    rev_trie = make_trie({}, rev_words)

    for query in queries:
        if query[0] == '?' and query[-1] == '?':
            answer.append(counted.count(len(query)))
        elif query[0] == '?':
            answer.append(search_trie(rev_trie, query[::-1], len(query)))
        elif query[-1] == '?':
            answer.append(search_trie(trie, query, len(query)))

    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"]	, ["fro??", "????o", "fr???", "fro???", "pro?"]	))