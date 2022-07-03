class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        repo = {}
        start = ord('a')
        for s in key:
            if s == ' ':
                continue
            if s not in repo:
                repo[s] = start
                start += 1
        
        ans = ""
        for s in message:
            if s == ' ':
                ans += ' '
                continue
            ans += chr(repo[s])
        
        return ans
