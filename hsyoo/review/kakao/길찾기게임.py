import sys
sys.setrecursionlimit(10 ** 6)

class Tree:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None
        self.right = None
        
def preorder(node, nodeinfo):
    pre_order_list.append(nodeinfo.index(node.data) + 1)
    if node.left != None:
        preorder(node.left, nodeinfo)
    if node.right != None:
        preorder(node.right, nodeinfo)

def postorder(node, nodeinfo):
    if node.left != None:
        postorder(node.left, nodeinfo)
    if node.right != None:
        postorder(node.right, nodeinfo)
    post_order_list.append(nodeinfo.index(node.data) + 1)
    
pre_order_list = []
post_order_list = []

def solution(nodeinfos):
    answer = []
    n_nodeinfos = sorted(nodeinfos, key = lambda x : (-x[1], x[0]))
    
    root = None
    for node in n_nodeinfos:
        if root == None:
            root = Tree(node)
        else:
            cur_node = root
            while True:
                if node[0] < cur_node.data[0] and cur_node.left != None:
                    cur_node = cur_node.left
                    continue
                elif node[0] < cur_node.data[0] and cur_node.left == None:
                    cur_node.left = Tree(node)
                    break
                elif node[0] > cur_node.data[0] and cur_node.right != None:
                    cur_node = cur_node.right
                    continue
                elif node[0] > cur_node.data[0] and cur_node.right == None:
                    cur_node.right = Tree(node)
                    break
    print(root.data, root.left.data, root.right.data)
    preorder(root, nodeinfos)
    postorder(root, nodeinfos)
    answer.append(pre_order_list)
    answer.append(post_order_list)
    return answer
    
print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]	))