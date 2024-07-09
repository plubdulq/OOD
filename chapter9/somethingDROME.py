def what_drome(data, count = 0,  drome = 'Repdrome'):
    if len(data) == count+1:
        return drome
    if data[count] == data[count+1]:
        if drome == 'Metadrome':
            return what_drome(data, count+1, 'Plaindrome')
        elif drome == 'Katadrome':
            return what_drome(data, count+1, 'Nialpdrome')
        return what_drome(data, count+1, drome)
    elif data[count] > data[count+1]:
        if drome in ['Metadrome', 'Plaindrome']:
            return f'Nondrome'
        if drome == 'Nialpdrome':
            return what_drome(data, count+1, drome)
        return what_drome(data, count+1, 'Katadrome')
    elif data[count] < data[count+1]:
        if drome in ['Katadrome', 'Nialpdrome']:
            return f'Nondrome'
        if drome == 'Plaindrome':
            return what_drome(data, count+1, drome)
        return what_drome(data, count+1, 'Metadrome')

inp = [int(x) for x in input('Enter Input : ')]
print(what_drome(inp))