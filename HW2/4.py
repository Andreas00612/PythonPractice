class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return

ans = []
def inOrderTraversal(root):
    if root is None:
	    return
    inOrderTraversal(root.left)
    ans.append(root.val)
    inOrderTraversal(root.right)
    return
def BSTCheck(root):
    #--- TO DO---#
    inOrderTraversal(root)
    for i in range(len(ans)-1):
        if ans[i]>=ans[i+1]:
          return False
    return True
    #------------------------------------------------------------#
#loading input file
with open('input.pkl','rb') as inp:
    tree = pickle.load(inp)
    print(BSTCheck(tree))