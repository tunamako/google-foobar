searchSize = 20232
integers = [True] * (searchSize + 1)
primes = ""

def answer(n):
	return primes[n:n+5]

for i in range(2, searchSize, 1):
	if len(primes) >= 10005:
		break
	if integers[i]:
		primes += str(i)
		for n in range(i * i, searchSize, i):
			integers[n] = False

print(answer(0))
print(answer(10000))