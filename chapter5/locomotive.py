class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
    
    def setNext(self, next):
        self.next = next

class LinkedList:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:
                t = t.next
                self.size += 1
            self.tail = t

    
    def __str__(self):
        s = ''
        t = self.head
        while t != None:
            s += str(t.data) + ' <- '
            t = t.next
        return s[:-4]
    
    def append(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next != None:
                t = t.next
            t.next = p
        self.size += 1

    def addHead(self, data):
        p = Node(data)
        if self.head is not None:
            p.next = self.head
            self.head = p
            self.size += 1
    
    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            p = self.head
            while p != None and p.next.data != data:
                p = p.next
                if p.next is None:
                    return
        p.next = p.next.next
        self.size -= 1
    
    def removeTail(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            p = self.head
            while p.next.next is not None:
                p = p.next
        p.next = p.next.next
        self.size -= 1
        return p.data

    def removeHead(self):
        if self.head is None:
            return
        if self.head.next is None:
            self.head = self.head.next
            return
        else:
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def size(self):
        return self.size

    def nodeAt(self, i):
        p = self.head
        for j in range(i):
            p = p.next
        return p
    
    def search(self, data):
        p = self.head
        while p is not None:
            if str(p.data) == str(data):
                return p
            p = p.next
        return None
    
    def isEmpty(self):
        return self.size == 0

print(" *** Locomotive ***")
linked_list = LinkedList()
inp = input('Enter Input : ').split()
for i in inp:
    linked_list.append(Node(i))
print(f'Before : {linked_list}')
for i in inp:
    if str(linked_list.search(i).data) != str(0):
        linked_list.append(linked_list.removeHead())
    else:
        break
print(f'After : {linked_list}')