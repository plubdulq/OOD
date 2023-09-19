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

    def preOrder(self, root, lst):
        if root is not None:
            lst.append(str(root.data))
            self.preOrder(root.left, lst)
            self.preOrder(root.right, lst)
            if len(lst) == len(inp):
                return f"Preorder : {' '.join(lst)}"
    def inOrder(self, root, lst):
        if root is not None:
            self.inOrder(root.left, lst)
            lst.append(str(root.data))
            self.inOrder(root.right, lst)
            if len(lst) == len(inp):
                return f"Inorder : {' '.join(lst)}"
    def postOrder(self, root, lst):
        if root is not None:
            self.postOrder(root.left, lst)
            self.postOrder(root.right, lst)
            lst.append(str(root.data))
            if len(lst) == len(inp):
                return f"Postorder : {' '.join(lst)}"
    
    def breadth(self, root):
        BFS = []
        if root is None:
            return
        queue = [root]
        
        while len(queue) > 0:
            cur_node = queue.pop(0)
            BFS.append(str(cur_node.data))

            if cur_node.left is not None:
                queue.append(cur_node.left)

            if cur_node.right is not None:
                queue.append(cur_node.right)
        return f"Breadth : {' '.join(BFS)}"
        
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i) #เขียนแค่ T.insert(i) ก็ได้
# T.printTree(T.root)
print(T.preOrder(T.root, []))
print(T.inOrder(T.root, []))
print(T.postOrder(T.root, []))
print(T.breadth(T.root))