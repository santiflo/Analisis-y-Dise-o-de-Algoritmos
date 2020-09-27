from sys import stdin

def solve(E,W):
	E.sort()
	ans,n,N = 0,0,len(E)
	while ans <= W and n!=N:
		if ans+E[n]<=W:
			ans += E[n]
			n += 1
		else: break
	return n

def main():
	casos = int(stdin.readline().strip())
	for _ in range(casos):
		X = stdin.readline().strip().split()
		M,W = int(X[0]), int(X[1])
		X = stdin.readline().strip().split()
		elephant = [int(w) for w in X]
		print(solve(elephant,W))

main()