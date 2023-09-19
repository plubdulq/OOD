class Queue:
    def __init__(self):
        self.queue = []

    def dequeue(self):
        return self.queue.pop(0)
    
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

q = Queue()
inp = input("Enter Input : ").split(',')
for i in inp:
    if i[0] == 'E':
        q.enqueue(i[2:])
        print(f'Add {i[2:]} index is {q.items().index(i[2:])}')
    else:
        if q.isEmpty():
            print('-1')
        else:
            dequeue = q.dequeue()
            print(f'Pop {dequeue} size in queue is {q.size()}')

if q.isEmpty():
    print('Empty')
else:
    print(f'Number in Queue is :  {q.items()}')
