def permutFunc(myList):

	# No permutations for empty list
	if len(myList) == 0:
		return []

	# Single permutation for only one element
	if len(myList) == 1:
		return [myList]

	# Permutations for more than 1 characters
	k = []

	# Looping
	for i in range(len(myList)):
		print(i)
		m = myList[i]
		res = myList[:i] + myList[i+1:]
		for p in permutFunc(res):
			k.append([m] + p)
	return k

# Driver program
myList = list('456')
for p in permutFunc(myList):
	print (p)