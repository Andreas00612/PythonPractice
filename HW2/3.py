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
def minDiff(root):
    #--- TO DO---#
    diff = []
    inOrderTraversal(root)
    for i in range(0,len(ans)-1):
        diff.append(ans[i+1]-ans[i])
    print(min(diff))

    #------------------------------------------------------------#
#loading input file
with open('input.pkl','rb') as inp:
    tree = pickle.load(inp)
    minDiff(tree)