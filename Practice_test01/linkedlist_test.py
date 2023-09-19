class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
class LinkedL:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
            return
        
        cur = self.head
        while cur != self.tail:
            cur = cur.next
        cur.next = newNode
        self.tail = newNode

    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s += str(cur.data) + '->'
            cur = cur.next 
        return s[:-2]
    
    def isEmpty(self):
        if self.head != None:
            return False
        return True
        
    
    def insert(self,pos,data):
        newNode = Node(data)
        index = 0
        cur = self.head
        if pos == 0:
            if self.isEmpty():
                self.tail = newNode
            newNode.next = self.head
            self.head = newNode
            
            return
        
        while pos-1 != index:
            index += 1
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode
        self.tail = newNode

    def search(self,data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def remove(self,data):
        cur = self.head
        while cur.data != data and cur != None:
            temp = cur
            cur = cur.next
            if cur.data == data:
                cd = cur.data
                temp.next = temp.next.next
                return cd
        prev_head = self.head
        self.head = self.head.next
        return prev_head.data
        
LL = LinkedL()
LL.insert(0,7)
LL.append(1)
LL.append(2)
LL.append(5)
LL.insert(0,4)
print(LL.search(4))
print(LL)
print(LL.remove(1))
print(LL)
        
        