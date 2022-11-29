
##########112801##########
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return


def minVal(root):
    # --- TO DO---#
    if root is None:
        return root
    if root.left is None:
        return root.val
    else:
        return minVal(root.left)

    # ------------------------------------------------------------#


# loading input file
with open('input.pkl', 'rb') as inp:
    tree = pickle.load(inp)
    print(minVal(tree))




##########112802<sol1>##########
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
def SearchForSix(root,target):
    #--- TO DO---#
    while root:
        n=root.val
        if n<target:
            root=root.right
        elif n>target:
            root=root.left
        elif n==target:
            return (inOrderTraversal(root))
with open('input.pkl','rb') as inp:
    tree = pickle.load(inp)
    SearchForSix(tree,6)
    if ans == []:
        print([None])
    else:
        print(ans)

##########112802<sol2>##########

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return


ans = []


def InOrderTraversal(root):
    # --- TO DO---#
    if root:
        InOrderTraversal(root.left)
        ans.append(root.val)
        InOrderTraversal(root.right)


def SearchForSix(root, target):
    if root is None:
        return []
    if target < root.val:
        SearchForSix(root.left, target)
    elif target > root.val:
        SearchForSix(root.right, target)
    else:
        return InOrderTraversal(root)

    # ------------------------------------------------------------#


# loading input file
with open('input.pkl', 'rb') as inp:
    tree = pickle.load(inp)
    SearchForSix(tree, 6)
    if ans == []:
        print([None])
    else:
        print(ans)