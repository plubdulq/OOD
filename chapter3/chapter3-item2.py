class Stack:
    def __init__(self):
        self.data = []
        self.par = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }
        self.all_par = '}{[()]'

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if not self.isEmpty():
            self.data.pop()

    def isEmpty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)

    def items(self):
        return self.data

def check_parentheses(expression):
    stack = Stack()
    error = None
    excess_count = 0

    for char in expression:
        if char in stack.all_par:
            if char in stack.par:
                stack.push(char)
                excess_count += 1
            elif stack.isEmpty():
                error = "close paren excess"
                excess_count = 0
            elif stack.par[stack.items()[-1]] == char:
                stack.pop()
                excess_count -= 1
            else:
                error = "Unmatch open-close"
                break
    if excess_count > 0 and error != "Unmatch open-close":
        error = f"open paren excess   {excess_count} : {'(' * excess_count}"
    if error is not None:
        return f"{expression} {error}"
    else:
        return f"{expression} MATCH"        
expression = input("Enter expresion : ")
result = check_parentheses(expression)
print(result)