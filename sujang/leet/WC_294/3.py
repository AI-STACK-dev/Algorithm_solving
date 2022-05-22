class Solution:
    def calculate_gradient_str(self, p1, p2):
        x = p2[0] - p1[0]
        y = p2[1] - p1[1]
        z = math.gcd(x,y)
        return str(y//z)+ "/" + str(x//z)

    def minimumLines(self, sps: List[List[int]]) -> int:
        sps.sort(key = lambda x: x[0])
        n = len(sps)
        ans = 0
        for i in range(n-1):
            a,b = i, i+1
            grad = self.calculate_gradient_str(sps[a],sps[b])
            if i == 0:
                prev = grad
                ans += 1
            else:
                if prev != grad:
                    ans += 1
                    prev = grad
        return ans
