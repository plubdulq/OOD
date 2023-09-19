class Stack:
    def __init__(self):
        self.data = []
    def push(self, i):
        self.data.append(i)
    def pop(self):
        self.data.pop()
    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.data)
    def items(self):
        return self.data

print(" *** Stack implement by Python list***")

ls = [e for e in input("Enter data to stack : ").split()]

s = Stack()

for e in ls:

    s.push(e)

print(s.size(),"Data in stack : ",s.items())

while not s.isEmpty():

    s.pop()

print(s.size(),"Data in stack : ",s.items())
