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
place = {
            0:'Res.',
            1:'ClassR.',
            2:'SuperM.',
            3:'Home'
        }
action = {
            0:'Eat',
            1:'Game',
            2:'Learn',
            3:'Movie'
        }
inp = input("Enter Input : ").split(',')
my_queue = queue()
ur_queue = queue()
myAct = ''
my_q = ''
urAct = ''
ur_q = ''
score = 0
for i in inp:
    my_queue.enqueue(i[:3])
    ur_queue.enqueue(i[4:])
for my in my_queue.items():
    my_q += f'{my}, '
    myAct += f'{action[int(my[0])]}:{place[int(my[-1])]}, '
for ur in ur_queue.items():
    ur_q += f'{ur}, '
    urAct += f'{action[int(ur[0])]}:{place[int(ur[-1])]}, '
for pos in range(my_queue.size()):
    if my_queue.items()[0][0] == ur_queue.items()[0][0] and my_queue.items()[0][2] == ur_queue.items()[0][2]:
        score += 4
    elif my_queue.items()[0][0] == ur_queue.items()[0][0]:
        score += 1
    elif my_queue.items()[0][2] == ur_queue.items()[0][2]:
        score += 2
    else:
        score -= 5
    my_queue.dequeue()
    ur_queue.dequeue()
    
if score >= 7:
    status = 'Yes! You' + '\'' + 're my love!'
elif score > 0:
    status = 'Umm.. It\'' + 's complicated relationship!'
else:
    status = 'No! We\'re just friends.'
print(f'My   Queue = {my_q[:-2]}')
print(f'Your Queue = {ur_q[:-2]}')
print(f'My   Activity:Location = {myAct[:-2]}')
print(f'Your Activity:Location = {urAct[:-2]}')
print(f'{status} : Score is {score}.')