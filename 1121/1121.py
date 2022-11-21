########112101########

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return
def postOrderTraversal(root):  
    #--- TO DO---#
    if root:
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        ans.append(root.val)
#loading input file
ans = []
with open('input.pkl','rb') as inp:
    tree = pickle.load(inp)
    postOrderTraversal(tree)
print(ans)

########112102########

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return
def postOrderTraversal(root):  
    #--- TO DO---#
    if root:
        ans.append(root.val)
        postOrderTraversal(root.left)
        postOrderTraversal(root.right)
        
#loading input file
ans = []
with open('input.pkl','rb') as inp:
    tree = pickle.load(inp)
    postOrderTraversal(tree)
print(ans)