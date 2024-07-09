class Node:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

def insertion(root, data):
    if root is None:
        return Node(data)
    if root.data < data:
        root.right = insertion(root.right, data)
    elif root.data > data:
        root.left = insertion(root.left, data)

    bf = balancing_boreye(root.left) - balancing_boreye(root.right)
    if bf > 1: #left
        lbf = balancing_boreye(root.left.left) - balancing_boreye(root.left.right)
        if lbf >= 0:
            root = rightRotate(root)
        elif lbf < 0:
            root.left = leftRotate(root.left)
            root = rightRotate(root)

    elif bf < -1: #right
        rbf = balancing_boreye(root.right.left) - balancing_boreye(root.right.right)
        if rbf > 0:
            root.right = rightRotate(root.right)
            root = leftRotate(root)
        elif rbf <= 0:
            root = leftRotate(root)
    return root

def leftRotate(root):
    y = root.right
    root.right = y.left
    y.left = root
    return y

def rightRotate(root):
    y = root.left
    root.left = y.right
    y.right = root
    return y

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node.data)
        printTree90(node.left, level + 1)

def getMinNode(root):
    if root.left is None or root is None:
        return root.data
    return getMinNode(root.left)

def balancing_boreye(root): #getHeight
    if root is None:
        return -1
    else:
        return max(balancing_boreye(root.left), balancing_boreye(root.right)) +1
    
def getHeight(root):
    if root is None:
        return -1
    return max(getHeight(root.left),getHeight(root.right))+1

inp = input('Enter Input : ').split()
root = Node(int(inp[0]))
for i in inp[1:]:
    root = insertion(root, int(i))
printTree90(root)
print(getMinNode(root))