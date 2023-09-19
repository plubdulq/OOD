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

inp = input("input : ").split(',')
q = queue()
err_de = 0
err_in = 0
num = 0
for action in inp:
    if action[0] == 'D':
        status = 'Dequeue : '
        for j in range(int(action[1])):
            if not q.isEmpty():
                q.dequeue()
            else:
                err_de += 1
    elif action[0] == 'E':
        status = 'Enqueue : '
        for j in range(int(action[1:])):
            q.enqueue(f'*{num}')
            num += 1
    else:
        status = ''
        err_in += 1
    print(f'Step : {action}')
    print(f'{status}{q.items()}')
    print(f'Error Dequeue : {err_de}')
    print(f'Error input : {err_in}')
    print('--------------------')