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
                #print(str(root.data) + ' ' + str(newNode.data) + 'l')
                if root.left is None:
                    root.left = newNode
                    return 
                root = root.left
            else:
                #print(str(root.data) + ' ' + str(newNode.data) + 'r')
                if root.right is None:
                    root.right = newNode
                    return 
                root = root.right
    def find_min(self):
        root = self.root
        while root is not None:
            if root.left is None:
                return root.data
            root = root.left
        return root.data
    
    def find_max(self):
        root = self.root
        while root is not None:
            if root.right is None:
                return root.data
            root = root.right
        return root.data

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
print('--------------------------------------------------')
print(f'Min : {T.find_min()}')
print(f'Max : {T.find_max()}')