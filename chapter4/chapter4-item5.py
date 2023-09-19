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
    
room = queue()
BFS_q = queue()
passed_q = queue()
x_pos = 0
y_pos = 0
Found_portal = False
valid_map = True
F_found = False
input = input("Enter width, height, and room: ").split(' ')
for i in [[j for j in i.split(',') if not i.isnumeric()]for i in input]:
    if i != []:
        std_len = len(i[0])
        for x in range(len(i)):
            if std_len != len(i[x]):
                valid_map = False
                break
            room.enqueue(i[x])
            if 'F' in room.items()[x]:
                F_found = True
                x_pos = room.items()[x].index('F')
                y_pos = x
                BFS_q.enqueue(f'({x_pos}, {y_pos})')
    if F_found == True and room.size() != int(input[1]):
        valid_map = False
if valid_map == True and F_found == True:
    while Found_portal == False: #เพิ่ม Found_portal + i < 13
        print(f"Queue: [{', '.join(BFS_q.items())}]")
        x_pos = int(BFS_q.items()[0][1])
        y_pos = int(BFS_q.items()[0][4])
        BFS_q.dequeue()
        #North
        if y_pos != 0 and room.items()[int(y_pos)-1][x_pos] in '_O' :
            if room.items()[int(y_pos)-1][x_pos] == 'O':
                print('Found the exit portal.')
                Found_portal = True
                break
            if not f'({x_pos}, {int(y_pos)-1})' in passed_q.items():
                BFS_q.enqueue(f'({x_pos}, {int(y_pos)-1})')
                passed_q.enqueue(f'({x_pos}, {int(y_pos)-1})')
        #East
        if x_pos != len(room.items()[0])-1 and room.items()[y_pos][int(x_pos)+1] in '_O' :
            if room.items()[y_pos][int(x_pos)+1] == 'O':
                print('Found the exit portal.')
                Found_portal = True
                break
            if not f'({int(x_pos)+1}, {y_pos})' in passed_q.items():
                BFS_q.enqueue(f'({x_pos+1}, {y_pos})')
                passed_q.enqueue(f'({x_pos+1}, {y_pos})')
        #South
        if y_pos != len(room.items())-1 and room.items()[int(y_pos)+1][x_pos] in '_O' :
            if room.items()[int(y_pos)+1][x_pos] == 'O':
                print('Found the exit portal.')
                Found_portal = True
                break
            if not f'({x_pos}, {int(y_pos)+1})' in passed_q.items():
                BFS_q.enqueue(f'({x_pos}, {int(y_pos)+1})')
                passed_q.enqueue(f'({x_pos}, {int(y_pos)+1})')
        #West
        if x_pos != 0 and room.items()[y_pos][int(x_pos-1)] in '_O' :
            if room.items()[y_pos][x_pos-1] == 'O':
                print('Found the exit portal.')
                Found_portal = True
                break
            if not f'({int(x_pos-1)}, {int(y_pos)})' in passed_q.items():
                BFS_q.enqueue(f'({int(x_pos-1)}, {int(y_pos)})')
                passed_q.enqueue(f'({int(x_pos-1)}, {int(y_pos)})')
        #Can't search more
        if BFS_q.size() == 0:
            print("Cannot reach the exit portal.")
            break
elif valid_map == False or F_found == False:
    print('Invalid map input.')