from collections import Counter
class Solution:
    def rearrangeCharacters(self, s, target):
        answer = []
        t = Counter(target)
        c = Counter(s)
        for key_ in t.keys():
            answer.append(c[key_] // t[key_])
        return min(answer)

print(Solution().rearrangeCharacters("ilovecodingonleetcode", "code"))
print(Solution().rearrangeCharacters("abcba", "abc"))
print(Solution().rearrangeCharacters("abbaccaddaeea", "aaaaa"))
        