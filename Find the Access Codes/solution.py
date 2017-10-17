def answer(L):
	divisorCount = [0] * len(L)
	tripleCount = 0
	for i in range(len(L)):
		for j in range(i):
			if L[i] % L[j] == 0:
				divisorCount[i] += 1
				tripleCount += divisorCount[j]
	return tripleCount

print(answer([1, 1, 1, 1]))
