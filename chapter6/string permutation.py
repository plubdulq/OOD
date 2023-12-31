def permute_string(lc: 'list[str]', k: int, s: int = 0) -> 'list[str]':
    if k == 0:
        return ['']
    answer = []
    for i in range(s, len(lc)):
        lc[s], lc[i] = lc[i], lc[s]
        part = permute_string(lc, k-1, s+1)
        for j in range(len(part)):
            part[j] = lc[s] + part[j]
        answer.extend(part)
    lc.append(lc.pop(s))
    return answer

s, k = input("Enter a string and k: ").split('/')
k = int(k)
if k < 0:
    print("Invalid value of k. k must be a non-negative integer.")
elif k > len(s):
    print('Invalid value of k. k must be less than or equal to the length of the string.')
else:
    print(sorted(set(permute_string(list(s), int(k)))))