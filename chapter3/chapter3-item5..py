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
    
action = input("Enter Input : ").split(',')
S = Stack()
for i in action:
    S.push(i.translate({ord(char): None for char in 'A '}))
    if i == 'B':
        seen_tree = 0
        S.pop()
        if not S.isEmpty():
            ref_tree = int(S.pop())
            S.push(ref_tree)
            seen_tree = 1
            check_rept = []
            for j in S.items():
                if ref_tree < int(j):
                    if int(j) not in check_rept:
                        seen_tree += 1
                    check_rept.append(j)
        print(seen_tree)
    if i == 'S':
        S.pop()
        if not S.isEmpty():
            for num in range(len(S.items())):
                if int(S.items()[num]) % 2 == 0:
                    S.items()[num] = int(S.items()[num])-1
                elif int(S.items()[num]) %2 != 0:
                    S.items()[num] = int(S.items()[num])+2