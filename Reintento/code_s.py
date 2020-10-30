from sys import stdin

"""
code = '123'
dictionary = {'1':'b', '2':'c', '3':'d', '23':'e', '12':'a'}
"""
dictionary = {}
code = ''
solutions = list()
cont = 0

def solve(n, word):
	global dictionary, code, solutions, cont
	if n==len(code):
		solutions.append(list(word))
		cont += 1
	else:
		if code[n] == '0' and int(code[n:])!=0:
			solve(n+1,word)
		i, temp = n+1, []
		while i <= len(code):
			if code[n:i] in dictionary:
				temp.append((str(dictionary[code[n:i]]), i))
			i += 1
		temp.sort()
		for w, j in temp:
			if cont < 100:
				solve(j,word+w)


"""
solve(0,'')
print(solutions)
"""
def main():
	global dictionary, code, solutions, cont
	N = int(stdin.readline().strip())
	case = 0
	while N!=0:
		case += 1
		for i in range(N):
			line = stdin.readline().strip().split()
			dictionary[line[1]] = line[0]
		code = stdin.readline().strip()
		print('Case #'+str(case))
		solve(0,'')	
		if len(solutions)!=0:
			for i in solutions:
				tem = ''
				for j in i:
					tem += j
				print(tem)
		else: print()
		print()
		dictionary.clear()
		solutions.clear()
		code = ''
		cont = 0
		N = int(stdin.readline().strip())

main()
