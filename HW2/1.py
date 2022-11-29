
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return

ans = []
def levelOrderTraversal(root):
    #--- TO DO---#
    if root is None:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        ans.append(node.val)
#------------------------------------------------------------#
#loading input file
with open('input.pkl','rb') as inp:
    tree = pickle.load(inp)
    levelOrderTraversal(tree)
    print(ans)
