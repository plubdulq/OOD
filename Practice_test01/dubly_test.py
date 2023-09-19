class Node:
    def __init__ (self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class Linkedlist:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def size(self):
        cur = self.head.next
        count = 0
        while cur is not self.tail:
            count += 1
            cur = cur.next
        return count

    def append(self, data):
        self.insert(self.size(), data)
    
    def isEmpty(self):
        if self.head.next != self.tail:
            return False
        return True

    def __str__(self):
        s = ''
        cur = self.head.next
        while cur is not self.tail:
            s += str(cur.data) + '->'
            cur = cur.next 
        return s[:-2]
    
    def insert(self,pos,data):
        newNode = Node(data)
        index = 0
        cur = self.head.next
        if pos == 0:
            newNode.next = cur
            cur.prev = newNode
            newNode.prev = self.head
            self.head.next = newNode
            return
        
        while pos-1 != index:
            index += 1
            cur = cur.next
        newNode.next = cur.next
        cur.next = newNode

    def search(self,data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return True
            cur = cur.next
        return False

    def remove(self,data):
        cur = self.head.next
        while cur.data != data and cur != None:
            temp = cur
            cur = cur.next
            if cur.data == data:
                cd = cur.data
                temp.next = temp.next.next
                return cd
        prev_head = cur
        self.head.next = prev_head.next
        return prev_head.data
    
    def index(self,data):
        cur = self.head.next
        idx = -1
        while cur is not self.tail:
            idx += 1
            if cur.data == data:
                return idx
            cur = cur.next
        
LL = Linkedlist()
LL.append(1)
LL.append(2)
LL.append(5)
LL.insert(0,4)
print(LL.search(4))
print(LL)
print(f'index is : {LL.index(2)}')
print(LL.remove(4))
print(f'index is : {LL.index(2)}')
print(LL)
        