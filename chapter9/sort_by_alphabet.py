def alphaSORT(data):
    alpha_lst = []
    cut = 0
    for idx in range(len(data)):
        for val in data[idx]:
            if val.isalpha():
                alpha_lst.append(val)
                break

    while cut != len(alpha_lst)-1:
        data[alpha_lst.index((max(alpha_lst[:len(alpha_lst)-cut])))], data[len(data)-cut-1] = data[len(data)-cut-1], data[alpha_lst.index((max(alpha_lst[:len(alpha_lst)-cut])))]
        alpha_lst[alpha_lst.index((max(alpha_lst[:len(alpha_lst)-cut])))], alpha_lst[len(alpha_lst)-cut-1] = alpha_lst[len(alpha_lst)-cut-1], alpha_lst[alpha_lst.index((max(alpha_lst[:len(alpha_lst)-cut])))]
        cut += 1
    return ' '.join(data)
    

inp = input('Enter Input : ').split(' ')
print(alphaSORT(inp))