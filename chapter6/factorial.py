def factorial(x):
    if x == 1 or x == 0:
        return 1
    else:
        return x*factorial(x-1)
inp = int(input('Enter Number : '))
print(f'{inp}! = {factorial(inp)}')