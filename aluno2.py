def maior(M):
	A=[]
	for i in range(len(M)):
		for a in range(len(M)):
			if M[i]>M[a] and a not in A:
				maior = M[i]
				A.append(a)
	return maior