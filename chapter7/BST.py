class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return 
        root = self.root
        while root is not None:
            if newNode.data < root.data:
                if root.left is None:
                    root.left = newNode
                    return 
                root = root.left
            else:
                if root.right is None:
                    root.right = newNode
                    return 
                root = root.right

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i) #เขียนแค่ T.insert(i) ก็ได้
T.printTree(T.root)
