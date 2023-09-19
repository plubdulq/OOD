def find_max_path(idx, path):
  global paths 

  if idx > len(inputs) - 1:
    if path not in paths:
      paths.append(path)
    return
 
  path_left = path.copy()
  path_right = path.copy()
  path_left.append(inputs[idx])
  path_right.append(inputs[idx])
  find_max_path(idx * 2 +1, path_left)
  find_max_path(idx * 2 +2, path_right)
  
inputs = [int(i) for i in input('Enter tree: ').split()]
paths = []

find_max_path(0, [])

max_path = []
max_sum = float('-inf')
for path in paths:
    if sum(path) > max_sum:
        max_sum = sum(path)
        max_path = path
  
print(f'Maximum path: {max_path}')