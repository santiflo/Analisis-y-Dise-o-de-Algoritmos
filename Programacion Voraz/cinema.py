from sys import stdin

brazo = [[0, 0, 0], [0, 0, 0]]
P = [['A3','-'],['B1','-'],['B4','-']]
Z = ['A1','A2','B2','B3']

def letra_a_numero(C):
	return ord(C)-ord('A')

#print(letra_a_row('C'))

def poner_gaseosa(A,silla,brazo):
	#print(A,silla,brazo)
	if brazo == '-': A[ silla[0]  ] [ silla[1]-1 ] = 1
	else: A[ silla[0] ] [ silla[1] ] = 1
	return A

#print('A1','+',poner_gaseosa(brazo,'A1','+'))
#print('A1','-',poner_gaseosa(brazo,'A1','-'))

def verificar_espacio(A,silla):
	if A[silla[0]][silla[1]-1] == 0: return '-'
	elif A[silla[0]][silla[1]] == 0: return '+'
	else: return 'x' 

def out_table(A):
	for i in A:
		temp = ''
		for j in i:
			temp += str(j)
		print(temp)

def out_list(A):
	for i in A:
	 	print(i)


def solve(R,C,P,Z):
	flag = True
	brazo = [[0 for _ in range(C+1)]for _ in range(R)]
	for p in P:
		brazo = poner_gaseosa(brazo, p[0], p[1])
	for z in Z:
		if (verificar_espacio(brazo, z) == '-'): brazo = poner_gaseosa(brazo, z, '-')
		elif(verificar_espacio(brazo, z) == '+'): brazo = poner_gaseosa(brazo, z, '+')
		else: 
			flag = False
			break
	return flag

def main():
	cont = 0
	X = stdin.readline().strip()
	while X != '0 0':
		cont += 1
		X = X.split()
		R, C = int(X[0]), int(X[1])
		X = int(stdin.readline().strip())
		P = [[] for _ in range(X)]
		for i in range(len(P)):
			p = stdin.readline().strip().split()
			p_row = letra_a_numero(p[0][0])
			p_col = int(p[0][1:])
			p[0] = [ p_row, p_col]
			P[i] = p
		X = int(stdin.readline().strip())
		Z = ['' for _ in range(X)]
		for i in range(len(Z)):
			z = stdin.readline().strip()
			z_row = letra_a_numero(z[0])
			z_col = int(z[1:])
			z = [z_row, z_col]
			Z[i] = z
		Z.sort()
		if solve(R,C,P,Z): print('YES')
		else: print('NO')
		X = stdin.readline().strip()

main()
#print(solve(3,5,P,Z))