def mergeSort(l, left, right):
    center = (left+right)//2
    if left < right:
        mergeSort(l,left,center)
        mergeSort(l,center+1,right)
        merge(l, left, center+1, right)

def merge(l,left,right,rightEnd):
    start = left
    leftEnd = right - 1
    result = []
    while left <= leftEnd and right <= rightEnd:
        if l[left] < l[right]:
            result.append(l[left])
            left += 1
        else:
            result.append(l[right])
            right += 1
    while left <= leftEnd:
        result.append(l[left])
        left += 1
    while right <= rightEnd:
        result.append(l[right])
        right += 1
    for ele in result:    
        l[start] = ele
        start += 1
        if start > rightEnd:
            break
sum = 0
a = []
b = []
sorted_a = []
non_sorted_b = []
inp = list(map(int,input('input : ').split()))
for i in range(len(inp)):
    if i%2 == 0:
        a.append(inp[i])
    else:
        b.append(inp[i])
        non_sorted_b.append(inp[i])
mergeSort(b, 0, len(b)-1)
for i in range(len(b)):
    sorted_a.append(a[non_sorted_b.index(b[i])])
for i in range(len(sorted_a)):
    for j in sorted_a[i+1:]:
        if sorted_a[i] > j:
            sum += sorted_a[i] + j
print(f'ans = {sum}')