from collections import Counter
class Solution:
    def percentageLetter(self, s, letter):
        c = Counter(s)
        per = int(c[letter] /len(s) * 100)
        return per

print(Solution().percentageLetter('foobar', 'o'))