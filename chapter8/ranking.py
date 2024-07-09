class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class BST:
    def __init__(self):
        self.root = None
    
    def add(self, data):
        newNode = Node(int(data))
        if self.root is None:
            self.root = newNode
            return

        root = self.root
        while root is not None:
            if root.data < newNode.data:
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
        if node is not None:
            self.printTree(node.left, level + 1)
            print('     '*level, node.data)
            self.printTree(node.right, level + 1)
    
    def find_rank(self, node, data):
        global rank
        if node is None:
            return
        self.find_rank(node.left, data)
        print(node.data)
        if node.data > data:
            rank -= 1
        self.find_rank(node.right, data)

bst = BST()
inp = input('Enter Input : ').split('/')
tree = inp[0].split(' ')
rank = len(tree)
for i in tree:
    bst.add(i)
bst.printTree(bst.root)
print('--------------------------------------------------')
bst.find_rank(bst.root, int(inp[1]))
print(f'Rank of {inp[1]} : {rank}')