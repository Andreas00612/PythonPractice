class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        return


def leafCount(root):
    # --- TO DO---#
    if root is None:
        return 0
    if root.left == None and root.right == None:
        return 1
    else:
        return leafCount(root.left) + leafCount(root.right)

    # ------------------------------------------------------------#


# loading input file
with open('input.pkl', 'rb') as inp:
    tree = pickle.load(inp)
    print(leafCount(tree))