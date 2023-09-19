class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.down = None
class Snode:
    def __init__(self,data):
        self.data = data
        self.down = None
class link:
    def __init__(self):
        self.head = self.tail = None

    def next_node(self,data):
        if self.search(data.data) == False:
            if self.head is None:
                self.head = data
                return
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = data

    def search(self,data):
        cur = self.head
        while cur is not None:
            if cur.data == data:
                return cur
            cur = cur.next
        return False

    def next_secondary_node(self,n,data):
        if self.search(n) is not False:
            temp = self.search(n)
            if temp.down is None:
                temp.down = data
                return
            while temp.down is not None:
                temp = temp.down
            temp.down = data

    def show_all(self):
        cur = self.head
        while cur is not None:
            temp = cur.next
            s = ''
            s += str(cur.data) + ' : '
            while cur.down is not None:
                s += str(cur.down.data) + ','
                cur = cur.down
            print(s)
            cur = temp
    
    def __str__(self):
        s = ''
        h = self.head
        while h is not None:
            s += str(h.data)  + "->"
            h = h.next
        return s[:-2]

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()