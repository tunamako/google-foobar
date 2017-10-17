#XOR is a neat choice by the security guards since it follows a simple pattern which maps easily to
#the integers mod 4. Using some simple algebra and taking advantage of the fact that XOR is
#commutative and associative, obtaining the XOR of a range of numbers is a cinch. 

def xorModulo(x):
	modFour = [x, 1, x+1, 0]
	return modFour[x%4]

def xorRange(a, b):
	return xorModulo(a - 1) ^ xorModulo(b)

#Running in linear time, this will obtain the XOR checksum of each row before combining it with
#the overall checksum, meaning only two XOR operations are performed per line of workers

def answer(start, length):
	idNumbers = []
	countDistance = length
	checksum = 0

	for i in range(start, start + length * length, length):
		checksum = checksum ^ xorRange(i, i + countDistance - 1)
		countDistance -= 1
	return checksum

#One step closer to freeing our bunnies :)