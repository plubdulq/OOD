print("*** String Rotation ***")
x, y = input("Enter 2 strings : ").split()
shifted_x = x
shifted_y = y
complete_loop = False
count = 0
while complete_loop == False:
    count += 1
    shifted_x = shifted_x[len(shifted_x)-2:]+shifted_x[0:len(shifted_x)-2]
    shifted_y = shifted_y[3:]+shifted_y[0]+shifted_y[1]+shifted_y[2]
    if count<=5:
        print(f'{count} {shifted_x} {shifted_y}')
        if count == 5:
            print(" . . . . . ")
    if shifted_x == x and shifted_y == y:
        if count>= 5:
            print(f'{count} {shifted_x} {shifted_y}')
        complete_loop = True
        break
print(f'Total of  {count} rounds.')



