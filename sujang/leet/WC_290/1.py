class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        repo = []
        for l in nums:
            l.sort()
            repo.append(set(l))
        
        ans = repo[0]
        for s in repo[1:]:
            ans &= s
        return sorted(list(ans))
