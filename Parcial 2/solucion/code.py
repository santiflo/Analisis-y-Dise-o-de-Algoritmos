import re

key = ['12', '1', '2', '3', '23']

value = list()

code = ''
key = list()
value = list()
solutions = list()

def solve(word, n):
	global solutions, key
	if n == len(code):
		solutions.append(list(word))
	else:
		i = n+1
		while i!=len(code):
			tem = list()
			for k in range(len(key)):
				if code[n:i] in key[k]:
					if len(key[k])==1:
					elif len(key[k]) == 2