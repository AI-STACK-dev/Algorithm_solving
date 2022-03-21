class Solution(object):
    def countCollisions(self, directions):
        directions = list(directions)
        ans = [0]*len(directions)

        # forward
        prev = directions[0]
        for i in range(1,len(directions)):
                if prev == 'R':
                    if directions[i] == 'L':
                        ans[i-1] = 1
                        ans[i] = 1
                        directions[i-1] = 'S'
                        directions[i] = 'S'
                    elif directions[i] == 'S':
                        ans[i-1] = 1
                        directions[i-1] = 'S'
                elif prev == 'S' and directions[i] == 'L':
                    ans[i] = 1
                    directions[i] = 'S'
                prev = directions[i]

        # backword
        prev = directions[-1]
        for i in range(len(directions)-2,-1,-1):
                if prev == 'L':
                    if directions[i] == 'R':
                        ans[i+1] = 1
                        ans[i] = 1
                        directions[i+1] = 'S'
                        directions[i] = 'S'
                    elif directions[i] == 'S':
                        ans[i+1] = 1
                        directions[i+1] = 'S'
                elif prev == 'S' and directions[i] == 'R':
                    ans[i] = 1
                    directions[i] = 'S'
                prev = directions[i]
        return sum(ans)