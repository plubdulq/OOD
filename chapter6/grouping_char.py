def grouping(index, length, count, x, y):
    y = str(y)

    if x[0] == y:
        count+=1
        if len(x) == 1:
            return count
    else:
        if length - len(x) > index-1:
            return count
        count = 0
    #print(x[0], y, count)
    return grouping(index, length, count,x[1:] ,y)
inp = input("input number : ").split(',')
if int(inp[1]) < 1 :
    print (f'Output : Pin number less than 1')
elif len(inp[0]) == 0:
    print (f'Output : List is entry')
elif int(inp[1]) > len(inp[0]):
    print (f'Output : Pin number out of range')
else:
    count = 0
    lenght = len(inp[0])
    print(f'Character : {inp[0][int(inp[1])-1]}')
    print(f'Count : {grouping(int(inp[1]), lenght, count, str(inp[0]), (inp[0][int(inp[1])-1]))}')