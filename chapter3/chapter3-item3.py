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

inp = input('Enter Input : ').split()
x = inp
S = Stack()
rep_char = 0
prev_char = ''
combo = 0
rept = False
while rept == False:
    check_rept = x
    for char in x:
        S.push(char)
        #print(S.size())
        if S.size() > 0:
            if prev_char == char:
                rep_char += 1
                if rep_char == 2:
                    combo += 1
                    rep_char = 0
                    for i in range(3):
                        S.pop()
            else:
                rep_char = 0
            prev_char = char
    x = []
    for i in range(S.size()):
        x.insert(0, S.pop())
        prev_char = ''
    if check_rept == x:
        for j in x:
            S.push(j)
        rept = True
print(S.size())                 
if S.size() > 0:
    for i in range(S.size()):
        print(S.pop(),end="")
else:
    print('Empty',end="")

if combo > 1:
    print(f'\nCombo : {combo} ! ! !')