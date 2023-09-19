def permute_string(s,k):
    k = int(k[0])
    if k<0:
        return "Invalid value of k. k must be a non-negative integer."
    elif k ==0:
        return ['']
    elif k>len(s):
        return 'Invalid value of k. k must be less than or equal to the length of the string.'
    else:
        return generate_permutations(s,k)

def generate_permutations(s,k):
    y = []
    for index in range(len(s)):
        print(index,end =',')
        start = s[index]
        remain = s[:index] + s[index+1:]
        for p in generate_permutations(remain,k):
            y.append([start] + p)
    return y


inp = input("Enter a string and k: ").split('/')
print(list(inp[0]), list(inp[1]))
# print(permute_string(str(inp[0]),int(inp[1])))
for p in permute_string(list(inp[0]),list(inp[1])):
    print(p)