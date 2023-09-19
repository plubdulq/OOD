def palindrom(input):
    if len(input) == 0 or len(input) == 1:
        return True
    
    if input[0] != input[len(input)-1]:
        return False
    
    if len(input) > 1:
        return palindrom(input[1:len(input)-1])
inp = input('Enter Input : ')
if palindrom(inp) == True:
    print(f"'{inp}' is palindrome")
else:
    print(f"'{inp}' is not palindrome")