print(" *** Divisible number ***")
x = 1
count = 0
output_list = []
num = int(input("Enter a positive number : "))
if num == 0:
    print("0 is OUT of range !!!")
else:
    while x<=num:
       if num%x == 0:
            output_list.append(x)
            count += 1
       x+=1
    print("Output ==> ",end="")
    for i in range(len(output_list)):
        print(output_list[i],end = " ")

    print("\n" + f'Total ==> {count}')