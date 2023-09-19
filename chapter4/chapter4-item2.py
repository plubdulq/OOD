class queue:
    def __init__(self):
        self.queue = []

    def dequeue(self):
        return self.queue.pop(0) if not self.isEmpty() else None
    
    def enqueue(self, value):
        return self.queue.append(value)
    
    def items(self):
        return self.queue
    
    def size(self):
        return len(self.queue)
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def peek(self):
        return self.queue[-1] if not self.isEmpty() else None

q = queue()
cashier1 = queue()
cashier2 = queue()
min = 0
min_cash2 = 0
inp = input("Enter people and time : ").split(' ')
for i in inp[0]:
    q.enqueue(i)
while min < int(inp[1]):
    min += 1
    if cashier2.size() > 0:
        min_cash2 += 1
    if min % 3 == 1 and cashier1.size() > 1:
        cashier1.dequeue()
    if min_cash2 % 2 == 0 and min_cash2 != 0:
        cashier2.dequeue()

    if cashier1.size() < 5 and not q.isEmpty():
        cashier1.enqueue(q.dequeue())
    elif cashier1.size() == 5 and not q.isEmpty():
        cashier2.enqueue(q.dequeue())
    
    print(f'{min} {q.items()} {cashier1.items()} {cashier2.items()}')