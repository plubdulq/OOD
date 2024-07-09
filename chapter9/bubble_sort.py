def bubble_sort(data, cut = 0, idx = 0):
    if idx == len(data) - cut -1:
        if len(data) - cut - 1 == 1:
            return data
        return bubble_sort(data, cut+1, 0)
    if data[idx] > data[idx+1]:
        data[idx],data[idx+1] = data[idx+1],data[idx]
        return bubble_sort(data, cut, idx+1)
    else:
        return bubble_sort(data, cut, idx+1)

inp = list(map(int, input('Enter Input : ').split()))
print(bubble_sort(inp))