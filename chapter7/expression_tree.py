class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class ExpressionTree:
    def __init__(self):
        self.root = None
    
    def buildTree(self, data):
        stack = []
        operation = ['+','-','*','/']

        for i in data:
            newNode = Node(i)
            if i not in operation:
                stack.append(newNode)
            else:
                newNode.right = stack.pop()
                newNode.left = stack.pop()
                stack.append(newNode)
        if stack:
            self.root = stack.pop()

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node.data)
            self.printTree(node.left, level + 1)

    def printInorder(self):
        self._printInorder(self.root)
    
    def _printInorder(self, node):
        if node is None:
            return
        if node.data in ['+','-','*','/']:
            print('(', end='')
        self._printInorder(node.left)
        print(node.data, end = '')
        self._printInorder(node.right)
        if node.data in ['+','-','*','/']:
            print(')', end='')

    def printPreorder(self):
        self._printPreorder(self.root)

    def _printPreorder(self, node):
        if node is None:
            return
        
        print(node.data, end='')
        self._printPreorder(node.left)
        self._printPreorder(node.right)


BST = ExpressionTree()
inp = input('Enter Postfix : ')
BST.buildTree(inp)
print('Tree : ')
BST.printTree(BST.root)
print('--------------------------------------------------')
print(f'Infix : ',end = '')
BST.printInorder()
print(f'\nPrefix : ',end='')
BST.printPreorder()