class Node:

    def __init__(self, data): 

        self.data = data  

        self.left = None  

        self.right = None 

        self.level = None 



    def __str__(self):

        return str(self.data) 



class Tree:

    def __init__(self): 

        self.root = None

        self.num = 0



    def insert(self, val):  

        if self.root == None:

            self.root = Node(val)

            self.num += 1

        else:

            h = height(self.root)

            max_node = pow(2,h+1)-1

            current = self.root

            if self.num+1 > max_node:

                while(current.left != None):

                    current = current.left

                current.left = Node(val)

                self.num+=1

            elif self.num+1 == max_node:
                
                while(current.right != None):

                    current = current.right

                current.right = Node(val)

                self.num+=1

            else:

                if self.num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

                    insert_subtree(current.left,self.num - round(pow(2,h)/2),val)

                else:

                    insert_subtree(current.right,self.num - pow(2,h),val)

                self.num+=1



def insert_subtree(r,num,val):

    if r != None:

        h = height(r)

        max_node = pow(2,h+1)-1

        current = r

        if num+1 > max_node:

            while(current.left != None):

                current = current.left

            current.left = Node(val)

            return

        elif num+1 == max_node:

            while(current.right != None):

                current = current.right

            current.right = Node(val)

            return

        if num+1 <= max_node-((max_node-(pow(2,h)-1))/2):

            insert_subtree(current.left,num - round(pow(2,h)/2),val)

        else:

            insert_subtree(current.right,num - pow(2,h),val)

    else:

        return



def height(root):

    if root == None:

        return -1

    else:

        left = height(root.left)

        right = height(root.right)

        if left>right:

            return left + 1

        else:

            return right + 1

                       

def printTree90(node, level = 0):

    if node != None:

        printTree90(node.right, level + 1)

        print('     ' * level, node)

        printTree90(node.left, level + 1)



# def check_binary_search_tree_(root, stack = [], idx = 0, count = 0):
#     if count == len(data):
#         return True
#     if root is not None:
#         if root.data > 100 or root.data < 0:
#             return False
#         if count == 0:
#             stack.append(root)
#         head = stack[count]
        
#         if head.left is not None:
#             if head.left.data > 100 or head.left.data < 0:
#                 return False
#             if head.data <= head.left.data :
#                 return False
#             idx += 1
#             stack.append(head.left)

#         if head.right is not None:
#             if head.right.data > 100 or head.right.data < 0:
#                 return False
#             if head.data >= head.right.data :
#                 return False
#             idx += 1
#             stack.append(head.right)
        
#         return check_binary_search_tree_(head, stack, idx, count+1)
    
def check_binary_search_tree_(root, stack = []):
    if root is not None:
        check_binary_search_tree_(root.left,stack)
        stack.append(root.data)
        if len(stack) == len(data):
            count = 0
            for i in stack:
                count += 1
                for j in stack[count:]:
                    if i >= j or i > 100 or i < 0:
                        print ('False')
                        return
            print('True')
        check_binary_search_tree_(root.right,stack)
        

tree = Tree()

data = input("Enter Input : ").split()

for e in data:

    tree.insert(int(e))

printTree90(tree.root)

check_binary_search_tree_(tree.root)