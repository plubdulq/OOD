class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.header = node(None)
        self.trailer = node(None)
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0
    
    def __str__(self):
        if self.isEmpty():
            return ''
        s = ''
        p = self.header.next
        while p.next != None:
            s += str(p.data) + '->'
            p = p.next
        return s[:-2]
    
    def str_reverse(self):
        if self.isEmpty():
            return ''
        s = ''
        p = self.trailer.prev
        while p.prev != None:
            s += str(p.data) + '->'
            p = p.prev
        return s[:-2]

    def isEmpty(self):
        return self.size == 0

    def append(self, data):
        self.insert(int(self.size), data)

    def insert(self, index, data):
        index = int(index)
        h = self.header
        p = node(data)
        if self.size < index or index < 0:
            return (f'Data cannot be added')
        else:
            if self.size == 0:
                p.next = h.next
                h.next.prev = p
                p.prev = h            
                h.next = p
                self.size += 1
            elif self.size > 0:
                if index >= 0:
                    for i in range(self.size+1):
                        if i == index:
                            p.next = h.next
                            h.next.prev = p
                            p.prev = h            
                            h.next = p
                        h = h.next
                self.size += 1
            return (f'index = {index} and data = {data}')
    
    def remove(self, data):
        h = self.header.next
        cnt = 0
        while h.next is not None:
            cnt += 1
            if str(h.data) == str(data):
                h.prev.next = h.prev.next.next
                h.prev.next.prev = h.prev
                self.size -= 1
                return (f'removed : {h.data} from index : {cnt-1}')
            h = h.next
        return (f'Not Found!')
           
dubly = DoublyLinkedList()
inp = input("Enter Input : ").split(',')
for i in inp: 
    for c in range(len(i)):
        if i[c].isalpha():
            if i[c] == 'A':
                if i[c+1] == 'b':
                    dubly.insert(0,int(i[c+3::]))
                else:
                    dubly.append(int(i[c+2::]))
            elif i[c] == 'I':
                temp = i[c+2:].split(':')
                print(dubly.insert(int(temp[0]),int(temp[1])))
            elif i[c] == 'R':
                print(dubly.remove(i[c+2::]))

            print(f'linked list : {dubly.__str__()}')
            print(f'reverse : {dubly.str_reverse()}')
            break