class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if not self.isEmpty():
            return self.data.pop()

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def size(self):
        return len(self.data)
    
    def items(self):
        return self.data
    
    def peek(self):
        return self.data[len(self.data)-1]
    
class StackCalc: ### class calculator
    def __init__(self):
        self.ans = ''
    def run(self, instructions):
        S = Stack()
        for i in instructions:
            if i.isalpha() == False or i == 'DUP' or i == 'POP' or i == 'PSH':
                if i.isnumeric():
                    S.push(i)
                if i == '+':
                    sum = int(S.pop()) + int(S.pop())
                    S.push(sum)
                if i == '-':
                    dif = int(S.pop()) - int(S.pop())
                    S.push(dif)
                if i == "*":
                    tim = int(S.pop()) * int(S.pop())
                    S.push(tim)
                if i == "/":
                    div = int(S.pop()) // int(S.pop())
                    S.push(div)
                if i == 'DUP':
                    S.push(S.peek())
                if i == 'POP':
                    S.pop()
                if i == 'PSH':
                    S.push(S.peek())

                if len(S.items()) != 0:
                    self.ans = S.peek()
                else:
                    self.ans = 0
            else:
                self.ans =  f'Invalid instruction: {i}'
                break
        
    def getValue(self):
        return self.ans
print("* Stack Calculator *")
arg = input("Enter arguments : ").split()
machine = StackCalc()
machine.run(arg)
print(machine.getValue())