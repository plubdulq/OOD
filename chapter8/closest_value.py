class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None

    def insert(self, Node):
        if self.root is None:
            self.root = Node
            return
        root = self.root
        while root is not None:
            if Node.data < root.data:
                if root.left is None:
                    root.left = Node
                    return
                root = root.left
            else:
                if root.right is None:
                    root.right = Node
                    return
                root = root.right

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

    def closestValue(self, root, value):
        if root is None:
            return
        stack.append(root)
        head = stack.pop()
        if head.data == value:
            closest[0] = value
            return
        else:
            if closest[0] > value:
                if head.data > value and head.data - value < closest[0] - value:
                    closest[0] = head.data
                elif head.data < value and value - head.data < closest[0] - value:
                    closest[0] = head.data
            else:
                if head.data > value and head.data - value < value - closest[0]:
                    closest[0] = head.data
                elif head.data < value and value - head.data < value - closest[0]:
                    closest[0] = head.data

        self.closestValue(head.left, value)
        self.closestValue(head.right,value)

stack = []
inp = input('Enter Input : ').split('/')
tree = inp[0].split(' ')
bst = BST()
for i in tree:
    bst.insert(Node(int(i)))
    bst.printTree(bst.root)
    print('--------------------------------------------------')
closest = [bst.root.data]
bst.closestValue(bst.root, int(inp[1]))
print(f'Closest value of {inp[1]} : {closest[0]}')