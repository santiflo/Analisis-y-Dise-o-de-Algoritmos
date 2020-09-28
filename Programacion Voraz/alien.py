from sys import stdin

S = ['as','sd','df','fg','gh']

def letra_a_mascara(C):
	C.lower()
	mask = '00000000000000000000000000'
	pos = ord(C)-ord('a')
	res = mask[:pos]+'1'+mask[pos+1:]
	return res

def A_or_B(A,B):
	tem = ''
	for i in range(26):
		if A[i]=='1' or B[i]=='1': tem += '1'
		else: tem += '0'
	return tem

def A_and_B(A,B):
	tem = ''
	for i in range(26):
		if A[i]=='1' and B[i]=='1': tem += '1'
		else: tem += '0'
	return tem 

def out_list(A):
	for i in A:
	 	print(i)

def alguna_concidencia(A,B):
	for i in range(26):
		if A[i]=='1' and A[i]==B[i]:  return True
	return False

def solve(S):
	n, N, cont = 0, len(S), 0
	best = S[n]
	while n<N-1:
		n += 1
		if alguna_concidencia(best,S[n]): best = A_and_B(best,S[n])
		else:
 			best = S[n]
 			cont += 1 
	return cont

def main():
	t = stdin.readline().strip()
	for i in range(int(t)):
		n = stdin.readline().strip()
		S = ['00000000000000000000000000' for _ in range(int(n))]
		for i in range(int(n)):
			secuencia = list(stdin.readline().strip())
			tem = '00000000000000000000000000'
			for j in secuencia:
				tem = A_or_B(tem,letra_a_mascara(j))
			S[i] = tem
		print(solve(S))
main()

#a = letra_a_mascara('a')
#b = letra_a_mascara('b')
#print(a)
#print(b)
#ab = A_or_B(a,b)
#ab = A_and_B(ab,b)
#print(ab)
#print(alguna_conciencia(b,ab))

#print('solucion -> ',solve(S))