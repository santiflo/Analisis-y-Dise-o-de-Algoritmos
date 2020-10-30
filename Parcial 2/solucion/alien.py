from sys import stdin

#base = ['as', 'sd', 'df', 'fg', 'gh']
#base = ['plum', 'orange', 'plum']

def solve(base):
	n, N, cont = 0, len(base), 0
	best = set(base[n])
	while n<N-1:
		n += 1
		if len(best & set(base[n]))>0:
			best = best & set(base[n])
		else:
			best = set(base[n])
			cont += 1
	return cont

#print(solve(base))

def main():
	line = stdin.readline().strip()
	for i in range(int(line)):
		line = stdin.readline().strip()
		base = []
		for i in range(int(line)):
			base.append(stdin.readline().strip())
		print(solve(base))

main()