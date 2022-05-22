class Solution:
    def tree_init(self, tree, idx, start, end, data):
        if start == end:
            tree[0][idx] = data[start]
            tree[1][idx] = data[start]
            return tree[0][idx],tree[1][idx]
        mid = (start+end)//2
        a,b = self.tree_init(tree, idx*2, start, mid, data)
        c,d = self.tree_init(tree,(idx*2)+1, mid+1, end, data)
        tree[0][idx] = min(a,c)
        tree[1][idx] = b + d
        return tree[0][idx],tree[1][idx]

    def tree_query(self, tree, idx, start, end, left, right):
        MAX = int(1e9)+1
        if end < left or start > right:
            return  [MAX,0]
        if left <= start and right >= end:
            return tree[0][idx],tree[1][idx]
        mid = (start+end)//2
        a,b = self.tree_query(tree, idx*2, start, mid, left, right)
        c,d = self.tree_query(tree, (idx*2)+1, mid+1, end, left, right)
        return min(a,c), b+d

    def totalStrength(self, s) -> int:
        n = len(s)
        segTree = [[0]*(n*4+1) for _ in range(2)]

        # Tree Init
        self.tree_init(segTree, 1, 0, n-1, s)

        ans = 0
        # Tree Query
        for i in range(n):
            for j in range(i,n):
                MIN,SUM = self.tree_query(segTree, 1, 0, n-1, i, j)
                ans += MIN*SUM
        
        return ans%(int(1e9)+7)


a = [1,3,1,2]
print(Solution().totalStrength(a))

