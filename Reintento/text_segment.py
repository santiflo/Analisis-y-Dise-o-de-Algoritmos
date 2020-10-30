A = 'artistoil'
dic = {'art', 'is', 'toil', 'artist', 'oil'}
def isword(i,j):
	global A, dic
	return A[i:j] in dic

def splitTableTestigo(i,w):
	global A
	ans = False
	if i == len(A): 
		print(w)
		ans = True
	else: 
		j = i + 1
		found = False
		while ans == False and j!=len(A)+1:
			if isword(i,j): 
				w.append(j)
				found = splitTableTestigo(j,w) or found
				w.pop()
			j += 1
		ans = found
	return ans

print(splitTableTestigo(0,[]))

def splitTable(i):
	global A
	ans = False
	if i == len(A): ans = True
	else: 
		j = i + 1
		while ans == False and j!=len(A)+1:
			if isword(i,j): 
				ans = splitTable(j)
			j += 1
	return ans

print(splitTable(0))

"""
	for j in range(i,len(A)+1):
		if isword(i,j):
			if splitTable(j):
				return True
"""