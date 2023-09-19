class node:
    def __init__(self, data ):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            p = self.head
            self.size = 1
            while p.next is not None:
                p = p.next
                self.size += 1
            self.tail = p
    
    def __str__(self):
        p = self.head
        s = ''
        while p is not None:
            s += str(p.data)+'->'
            p = p.next
        return s[:-2]

    def append(self,data):
        new_node = node(data)
        if self.size == 0:
            self.head = new_node
        else:
            p = self.head
            while p.next is not None:
                p = p.next
            p.next = new_node
        self.size += 1
    
    def addHead(self,data):
        p = node(data)
        if self.size == 0:
            self.append(data)
        else:
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
    
    def nodeAt(self,i):
        p = self.head
        for j in range(i):
            p = p.next
        return p
    
    def search(self,data):
        p = self.head
        while p is not None:
            if str(p.data) == str(data):
                return p
            p = p.next
        return 
all_bokies = []
full_boky_list = []
ans_list = []
count = -1
ans_count = 0
inp = [[y for y in x.split(',')] for x in input("Enter input: ").split(' ')]
for i in range(1,(int(inp[0][0]))+1):
    all_bokies.append(str(i))
for i in inp[1]:
    ll = linked_list()
    boky_ref = i.split('-')
    if boky_ref[0] != boky_ref[1]:
        ll.addHead(boky_ref[0])
        ll.append(boky_ref[1])
        count += 1
        if count != len(inp[1]):
            change_ll = True
            j = -1
            while change_ll == True:
                j += 1
                boky_con = inp[1][j].split('-')
                if boky_ref[0] == boky_con[1] and boky_ref[0] != boky_con[0]:
                    ll.addHead(boky_con[0])
                    boky_ref[0] = boky_con[0]
                    j = -1
                elif boky_ref[1] == boky_con[0] and boky_ref[1] != boky_con[1]:
                    ll.append(boky_con[1])
                    boky_ref[1] = boky_con[1]
                    j = -1
                elif j == len(inp[1])-1:
                    change_ll = False
            if len(full_boky_list) == 0:
                full_boky_list.append(str(ll))
            else:
                token = 0
                for k in full_boky_list:
                    if str(ll).split('->')[0] in str(k.split('->')):
                        break
                    else:
                        token += 1
                    if token == len(full_boky_list):
                        full_boky_list.append(str(ll))
for x in all_bokies:
    appear_node = False
    for y in full_boky_list:
        if int(x) == int(y.split('->')[0]):
            appear_node = True
            ans_list.append(y)
            #print(x, y, y.split('->')[0], type(x), type(y.split('->')[0]))
            break
        if x in y.split('->'):
            appear_node = True
    if appear_node == False:
        ans_list.append(x)
for i in ans_list:
    ans_count += 1
    print(f'{ans_count}: {i}')
print(f'Number of train(s): {ans_count}')