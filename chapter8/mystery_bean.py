class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def _addNode(self, Node):
        if self.root is None:
            self.root = Node
            print('*')
            return
        root = self.root
        while root is not None:
            if Node.data < root.data:
                print('L',end = '')
                if root.left is None:
                    root.left = Node
                    print('*')
                    return
                root = root.left
            else:
                print('R',end = '')
                if root.right is None:
                    root.right = Node
                    print('*')
                    return
                root = root.right
                
inp = input('Enter Input : ').split()
bst = BST()
for i in inp:
    bst._addNode(Node(int(i)))