class Solution(object):
    def digArtifacts(self, n, artifacts, dig):
        field = [[0]*n for _ in range(n)]
        for i,(ux,uy,dx,dy) in enumerate(artifacts):
            for x in range(ux,dx+1):
                for y in range(uy,dy+1):
                    field[x][y] = i+1
        
        for digx,digy in dig:
            field[digx][digy] = 0


        temp = set()
        for i in range(n):
            for j in range(n):
                if field[i][j] != 0:
                    temp.add(field[i][j])
        
        return len(artifacts) - len(temp)
