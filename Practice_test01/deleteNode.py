class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.data)

class AVL_Tree():
    def __init__(self):
        self.root = None

    def _insert(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self._insert(root.left, data)
        else:
            root.right = self._insert(root.right, data)
        
        bf = self.getbalance(root)
        if bf > 1: # left
            lbf = self.getbalance(root.left)
            if lbf >= 0:
                return self.rotateright(root)

            elif lbf < 0:
                root.left = self.rotateleft(root.left)
                return self.rotateright(root)

        elif bf < -1: # right
            rbf = self.getbalance(root.right)
            if rbf > 0:
                root.right = self.rotateright(root.right)
                return self.rotateleft(root)

            elif rbf <= 0:
                return self.rotateleft(root)

        return root

    def _delete(self, root, data):
        if root is None:
            return None
        if data < root.data:
            root.left = self._delete(root.left, data)

        elif data > root.data:
            root.right = self._delete(root.right, data)

        else:
            if root.left and root.right:
                suc = self.getMinNode(root.right)
                root.data = suc.data
                root.right = self._delete(root.right, suc)

            elif root.left is not None:
                return root.left
            
            elif root.right is not None:
                return root.right
            
            else:
                return None
        
        bf = self.getbalance(root)
        if bf > 1: # left
            lbf = self.getbalance(root.left)
            if lbf >= 0:
                return self.rotateright(root)

            elif rbf < 0:
                root.left = self.rotateleft(root.left)
                return self.rotateright(root)

        elif bf < -1: # right
            rbf = self.getbalance(root.right)
            if rbf > 0:
                root.right = self.rotateright(root.right)
                return self.rotateleft(root)

            elif rbf <= 0:
                return self.rotateleft(root)

        return root

    def getMinNode(self, root):
        if root is None or root.left is None:
            return root
        
        return self.getMinRoot(root.left)

    def delete(self, data):
        self.root = self._delete(self.root, data)

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def height(self, node):
        if node is None:
            return 0
        
        left = self.height(node.left)
        right = self.height(node.right)
        if left > right:
            val = left + 1

        else:
            val = right + 1

        return val
    
    def printTree(self, root, level = 0):
        if root is not None:
            self.printTree(root.right, level + 1)
            print('    ' * level, root.data,f"({self.height(root)}),({self.getbalance(root)})")
            self.printTree(root.left, level + 1)
    '''
        y                            x
       / \     Right Rotation       / \ 
      x   C    - - - - - - - >     A   y
     / \       < - - - - - - -        / \ 
    A   B      Left Rotation         B   C
    '''
    def getbalance(self, root):
        return self.height(root.left)-self.height(root.right)

    def rotateleft(self, root):
        y = root.right
        root.right = y.left
        y.left = root
        return y
    
    def rotateright(self, root):
        x = root.left
        root.left = x.right
        x.right = root
        return x
    
tree = AVL_Tree()
inp = input("Enter Input : ").split()
for i in inp:
    tree.insert(int(i))
tree.printTree(tree.root)