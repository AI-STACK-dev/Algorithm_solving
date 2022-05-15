from collections import Counter

# words = ["abba","baba","bbaa","cd","cd"]
words = ["a","b","c","d","e"]
n = len(words)

answer = [words[0]]
for idx in range(1, n):
    c1 = Counter(words[idx-1])
    c2 = Counter(words[idx])
    if c1 != c2:
        answer.append(words[idx])
# print(answer)

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        n = len(words)
        answer = [words[0]]
        for idx in range(1, n):
            c1 = Counter(words[idx-1])
            c2 = Counter(words[idx])
            if c1 != c2:
                answer.append(words[idx])
        return answer