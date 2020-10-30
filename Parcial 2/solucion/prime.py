from sys import stdin
#Memoria que almacenara la respuesta de cada caso de prueba	
memory = []
#Primos que se pueden generar hasta 31
prime = [2,3,5,7,11,13,17,19,23,29,31]
#Posibles numeros que pueden sumarse a un indice i que generan un primo
possible = [[],						#Para 0
			[2, 4, 6, 10, 12, 16],	#Para 1
			[1, 3, 5, 9, 11, 15],	#Para 2
			[2, 4, 8, 10, 14, 16], 	#Para 3
			[1, 3, 7, 9, 13, 15],	#Para 4
			[2, 6, 8, 12, 14],		#Para 5
			[1, 5, 7, 11, 13],		#Para 6
			[4, 6, 10, 12, 16],		#Para 7
			[3, 5, 9, 11, 15],		#Para 8
			[2, 4, 8, 10, 14], 		#Para 9
			[1, 3, 7, 9, 13], 		#Para 10
			[2, 6, 8, 12],			#Para 11
			[1, 5, 7, 11], 			#Para 12
			[4, 6, 10, 16],			#Para 13
			[3, 5, 9, 15],			#Para 14
			[2, 4, 8, 14, 16], 		#Para 15
			[1, 3, 7, 13, 15]]		#Para 16

def is_prime(x):
	global prime
	return x in prime

for i in range(1,17):
	tem = ''
	for j in range(1,17):
		if is_prime(i+j): tem += str(j) + ' ' 
	print(i, tem)

"""
def solve(N, n, circle):
	global memory, prime, possible
	if n == N and is_prime(circle[0]+circle[-1]):
		memory.append(list(circle))
	else:
		for i in possible[circle[-1]]:
			if not(i in circle) and i<=N:
				circle.append(i)
				solve(N, n+1, circle)
				circle.pop()

#solve(8, 1, [1])

def main():
	global memory
	line = stdin.readline().strip()
	case = 0
	while len(line)!=0:
		case += 1
		solve(int(line),1, [1])
		print('Case '+str(case)+':')
		for i in memory:
			tem = ''
			for j in i:
				tem += str(j)+' '
			print(tem)
		memory.clear()
		print()
		line = stdin.readline().strip()

main()
"""