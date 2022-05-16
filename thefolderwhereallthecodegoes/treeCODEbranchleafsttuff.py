class treeNode:
    def __init__(self,data):
        self.left = None
        self.right = None 
        self.data = data
root = treeNode(10)
root.left = treeNode(15)
root.left.left = treeNode(9)
root.left.right = treeNode(16)

def plussxssTree(root):
    total = 0 
    if root is not None:
        total += plussxssTree(root.left)
        total += plussxssTree(root.right)
        total += root.data
    return total 

print(plussxssTree(root))

