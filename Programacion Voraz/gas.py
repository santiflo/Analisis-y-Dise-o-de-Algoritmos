from sys import stdin

gas = [[5,5],[20,10],[40,10]]
low = 0
hi = 40

def solve(A,L,H):
	A.sort()
	ans,low,n,N = list(),L,0,len(A)
	while low<H and n!=N:
		best, n = n, n+1
		if A[best][0]>low : return -1
		while n!=N and A[n][0]<=low:
			if A[n][1]>A[best][1]:
				best = n
			pass
			n+=1
		pass
		ans.append(best)
		low = A[best][1]
	if low < H : return -1
	return len(A)-len(ans)

def main():
	X = stdin.readline().strip()
	while X != '0 0':
		X = X.split()
		L =  int(X[0])							#Longitud de la carretera
		covertura = [[] for _ in range(int(X[1]))]	#Estaciones de gasolina
		for i in range(int(X[1])):
			gas = stdin.readline().strip().split()
			covertura[i] = [int(gas[0])-int(gas[1]), int(gas[0])+int(gas[1])]	#Rango de covertura de cada estacion de gasolina
		pass
		print(solve(covertura,0,L))
		X = stdin.readline().strip()	

main()