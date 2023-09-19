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
        self.head = node(None)

    def next_node(self,data):
        if self.search(data.data):
            return
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = data

    def search(self,data):
        p = self.head
        while p and p.data != data:
            p = p.next
        return p

    def next_secondary_node(self,n,data):
        p = self.search(n)
        if p != self.head:
            while p.down is not None:
                p = p.down
            p.down = data

    def show_all(self):
        p = self.head.next
        while p is not None:
            print(f'{p.data} : ',end='')
            p_down_node = p.down
            while p_down_node is not None:
                print(f'{p_down_node.data},',end='')
                p_down_node = p_down_node.down
            print()
            p = p.next

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