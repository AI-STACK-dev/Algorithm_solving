class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        field = [[0]*201 for _ in range(201)]
        ans = 0
        for x,y,r in circles:
            for i in range(x-r,x+r+1):
                for j in range(y-r,y+r+1):
                    if (i-x)**2 + (j-y)**2 <= r**2:
                        if field[i][j] == 0:
                            ans += 1
                            field[i][j] = 1
        return ans
