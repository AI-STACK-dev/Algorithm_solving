class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]

        field = [[-1]*n for _ in range(m)]

        point = [0,0]
        dirc = 0        
        while True:
            if head == None:
                break
            element = head.val
            field[point[0]][point[1]] = element

            if 0 > point[0]+dx[dirc] or m <= point[0]+dx[dirc] or 0 > point[1]+dy[dirc] or n <= point[1]+dy[dirc] or field[point[0]+dx[dirc]][point[1]+dy[dirc]] != -1:
                dirc = (dirc + 1) % 4
            point[0] += dx[dirc]
            point[1] += dy[dirc]

            head = head.next

        return field
