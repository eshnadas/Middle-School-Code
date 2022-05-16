class treeNode:
    def __init__(self,data):
        self.left = None
        self.right = None 
        self.data = data
        self.height = 1
class AVLTree: 
    def __init__(self):
        self.root = None

    def insert(self,root, value):
        if self.root is None:
            self.root = treeNode(value)
            return 
        if root is not None:    
            if value < root.data:
                root.left = self.insert(root.left , value)
            elif value > root.data:
                root.right = self.insert(root.right, value)
            root.height = 1 + max(root.left.height, root.right.height) 
        balance = root.left.height - root.right.height
        if balance > 1:
            return self.rightrotate(root)
        if balance < -1: 
            return self.leftrotate(root)
    
        else: 
            return treeNode(value)
        return root

    def rightrotate(self, a):
        b = a.left
        d = b.right
        b.right = a 
        a.left = d
        return b
    def leftrotate(self,a):
        b = a.right
        b.left = c
        b.right = d
        b.left = a
        a.right = c
        return b 


tree = AVLTree ()
# tree.insert(tree.root, "sally")
# tree.insert(tree.root, "karen")
# tree.insert(tree.root, "mr Wittmayer")
# tree.insert(tree.root, "esHNA")
# tree.insert(tree.root, "beth")
# tree.insert(tree.root, "bob")
# tree.insert(tree.root, "sally")
# tree.insert(tree.root, "chikki")
# tree.insert(tree.root, "panda")
# tree.insert(tree.root, "adaline")
# tree.insert(tree.root, "sasha")
# tree.insert(tree.root, "sonia")
tree.insert(tree.root, 4)
tree.insert(tree.root,2)
tree.insert(tree.root,1)
tree.insert(tree.root,3)
tree.rightrotate(tree.root)
print("empty")
