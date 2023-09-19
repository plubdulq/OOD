class Stack:
    def __init__(self):
        self.data = []
    
    def push(self, i):
        self.data.append(i)
    
    def pop(self):
        self.data.pop()
    
    def isEmpty(self):
        return len(self.data) == 0
    
    def size(self):
        return len(self.data)

class parenthesis:
    def __init__(self):
        self.pars = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        self.all_par = '({[]})'
    
    def matching(self, inp):
        s = Stack()
        open_par = False
        close_par = False
        for i in inp:
            if i in self.all_par:
                if i in self.pars.values():
                    s.push(i)
                elif not s.isEmpty() and self.pars[i] == s.data[-1]:
                    s.pop()   
                else:
                    s.push(i)
        if s.size() == 0:
            return (f'{inp} MATCH')
        else:
            for i in s.data:
                if i in self.pars.values(): #([]])( wrong output
                    open_par = True
                if i in self.pars:
                    close_par = True
            if open_par == True and close_par == True:
                return f'{inp} Unmatch open-close'
            elif s.data[-1] in self.pars:
                return f'{inp} close paren excess'
            elif s.data[-1] in self.pars.values():
                return f'{inp} open paren excess   {s.size()} : {"".join(s.data)}'

inp = input("Enter expression : ")
Parenthesis = parenthesis()
print(Parenthesis.matching(inp))