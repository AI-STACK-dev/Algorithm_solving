"""
이 문제로 얻은 점.
1. 트리의 개념 -> 이진트리
2. index연산할 때, 리스트[x,y]형태도 찾는다.
여러번 복습하면서 공부해야할 스탠다드 코드
"""
import sys
sys.setrecursionlimit(10**6)

class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

preorder_list = []
postorder_list = []

def preorder(node, nodeinfo):
    preorder_list.append(nodeinfo.index(node.data) + 1)
    if node.left:
        preorder(node.left, nodeinfo)
    if node.right:
        preorder(node.right, nodeinfo)

def postorder(node, nodeinfo):
    if node.left:
        postorder(node.left, nodeinfo)
    if node.right:
        postorder(node.right, nodeinfo)
    postorder_list.append(nodeinfo.index(node.data) + 1)

def solution(nodeinfo):
    """
    nodeinfo[i]는 i+1번 노드의 좌표이며, [x축 좌표, y축 좌표]를 의미, y축 좌표는 level
    """
    answer = []
    # y값이 제일 높은 게 맨 앞, 그리고 x좌표 순서대로 정렬하기
    sorted_node_info = sorted(nodeinfo, key = lambda x : (-x[1], x[0]))
    
    root = None
    for node in sorted_node_info:
        if not root:
            root = Tree(node) # data로 좌표가 들어간다.
        else:
            current = root
            while True:
                if node[0] < current.data[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break
                if node[0] > current.data[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break
                break
    preorder(root, nodeinfo)
    postorder(root, nodeinfo)
    answer.append(preorder_list)
    answer.append(postorder_list)

    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	))