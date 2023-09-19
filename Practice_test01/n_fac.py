class Stack():
    def __init__(self):
        self.items = []
      
    def push(self, i):
        self.items.append(i)
    
    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        return self.items[-1]
    
    def size(self):
        return len(self.items)
    
s = Stack()
l = [1,2,3,4,'5']
for i in l:
    s.push(i)
print(s.items)
print(s.items[s.size()-1])
print(s.pop())
print(s.items)
print(s.isEmpty())
print(s.peek())