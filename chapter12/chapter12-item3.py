print(" *** String count ***")
message = input("Enter message : ")
message_list = []
message_list.extend(message)
message_list.sort()
uppercase = 0
up_lst = []
lowercase = 0
low_lst = []
for i in range(len(message_list)):
    if message_list[i].isupper():
        uppercase += 1
        up_lst.append(message_list[i])
        for j in range(len(up_lst)):
            if j < len(up_lst)-1 and message_list[i] == up_lst[j]:
                up_lst.pop()
                break 
    if message_list[i].islower():
        lowercase += 1
        low_lst.append(message_list[i])
        for k in range(len(low_lst)):
            if k < len(low_lst)-1 and message_list[i] == low_lst[k]:
                low_lst.pop()
                break
print(f'No. of Upper case characters : {uppercase}')
print("Unique Upper case characters :",end=" ")
for x in up_lst:
    print(x,end="  ")
print('\n' + f'No. of Lower case Characters : {lowercase}')
print("Unique Lower case characters :",end=" ")    
for x in low_lst:
    print(x,end="  ")    