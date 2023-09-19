class Stack:
    def __init__(self):
        self.data = []

    def push(self,value):
        self.data.append(value)
    
    def pop(self):
        self.data.pop()
    
    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

class Parenthesis:
    def __init__(self):
        self.parent = {
            ')' : '(',
            ']' : '['
        }
    def parenthesis_pair(self, pars):
        s = Stack()
        for par in pars:
            if par in self.parent.values():
                s.push(par)
            elif not s.isEmpty() and self.parent[par] == s.data[-1]:
                s.pop()
            else:
                s.push(par)
        print(s.size())
        if s.size() == 0:
            print('Perfect ! ! !')
inp = input("Enter Input : ")
paren = Parenthesis()
paren.parenthesis_pair(inp)
