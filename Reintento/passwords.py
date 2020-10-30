from sys import stdin

dictionary = ['root', '2super']
rule = ['#0']

def solve(dictionary, rule):
	password = [[] for _ in range(len(rule))]
	for i in range(len(rule)):
		password[i].append('')
	i = 0
	while i<len(rule):
		for r in list(rule[i]):
			tem = list()
			if r=='#':
				for p in password[i]:
					for d in dictionary:
						tem.append(p+d)
			if r=='0':
				for p in password[i]:
					for n in range(10):
						tem.append(p+str(n))
			password[i] = tem
		i+=1
	return password

def main():
	line = stdin.readline().strip()
	while len(line)!=0:
		n = int(line)
		dictionary = list()
		for i in range(n):
			dictionary.append(stdin.readline().strip())
		m = int(stdin.readline().strip())
		rule = list()
		for i in range(m):
			rule.append(stdin.readline().strip())
		for p in solve(dictionary, rule):
			print('--')
			for ans in p: print(ans)
		line = stdin.readline().strip()



main()