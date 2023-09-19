def power(x, y):
    if y == 0:
        return 1
    else:
        return x*power(x, y-1)
inp = input("Enter Input a b : ").split(' ')
print(power(int(inp[0]), int(inp[1])))