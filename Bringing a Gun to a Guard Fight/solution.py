import math

#Credit to http://joncole.me/pages/reflector/  for providing a tool that led me to discover
#the secret behind solving this problem. Lets put this beam weapon to good use!

def gcd(a, b):
	if min(a,b) == 0:
		return max(a, b)
	while b:
		a, b = b, a%b
	return a

class VectorList:
	def __init__(self, captain, beamLength):
		self.vectors = {}
		self.suicideVectors = {}
		self.captain = captain
		self.beamLength = beamLength

	def vectorCount(self):
		return len(self.vectors)

	def addVector(self, x, y, isSuicide = False):
		v = self.generateVector(x,y)
		if v == None: return

		vectors = self.suicideVectors if isSuicide else self.vectors

		if v[0] in vectors:
			vectors[v[0]] = min(vectors[v[0]], v[1])
		else:
			vectors[v[0]] = v[1]

	def generateVector(self, x, y):
		bearing = (x - self.captain[0], y - self.captain[1])
		mag = math.sqrt((bearing[0]) ** 2 + (bearing[1]) ** 2)

		if (bearing[0] == 0 and bearing[1] == 0) or mag > self.beamLength:
			return
		else:
			g = gcd(abs(bearing[0]), abs(bearing[1]))

		v = [(bearing[0]/g, bearing[1]/g), mag]

		return v

	#We dont want to kill ourselves
	def removeSuicides(self):
		for s in self.suicideVectors:
			if s in self.vectors:
				if self.vectors[s] > self.suicideVectors[s]:
					self.vectors.pop(s)



#Here we search a square space of "parallel" rooms where the alternate versions of 
#the captain and the guard exist, with the dimensions of the square being the maximum
#amount of parallel rooms the beam can cover. I considered having a circular search
#space to reduce the amount of wasted searches, but the implementation ended up 
#being slower than what's below.
def answer(room, captain, guard, beamLength):
	m, n = room[0], room[1]
	captain_x, captain_y = captain[0], captain[1]
	guard_x, guard_y = guard[0], guard[1]
	vectors = VectorList(captain, beamLength)

	xBoxes = beamLength/m + 1
	yBoxes = beamLength/n + 1

	for i in xrange(-1 * xBoxes, xBoxes + 2, 1):
		for j in xrange(-1 * yBoxes, yBoxes + 2, 1):
			i_odd = abs(i) % 2
			j_odd = abs(j) % 2
			offsetX, offsetY = ((i + i_odd) * m), ((j + j_odd) * n)
			mirrorPosX, mirrorPosY = (-2 * i_odd + 1), (-2 * j_odd + 1)

			guardCoords = (
				offsetX + mirrorPosX * guard_x,
				offsetY	+ mirrorPosY * guard_y
			)
			myCoords = (
				offsetX + mirrorPosX * captain_x,
				offsetY	+ mirrorPosY * captain_y
			)
			vectors.addVector(guardCoords[0], guardCoords[1], False)
			vectors.addVector(myCoords[0], myCoords[1], True)

	vectors.removeSuicides()
	return vectors.vectorCount()


tests = [
	[
		[3, 2],
		[1, 1],
		[2, 1],
		400
	],
]


results = [0 for x in range(len(tests))]
answers = [6, 16, 935, 2789, 2000000000, 23, 256, 141031256]
timingsSum = [0 for x in range(len(tests))]
testRuns = 10

for j in range(1, testRuns + 1):
	print("Testing round: " + str(j))
	for i in range(len(tests)):
		start = time.time()
		results[i] = answer(tests[i][0], tests[i][1], tests[i][2], tests[i][3])
		timingsSum[i] += time.time() - start

for i, t in enumerate(timingsSum):
	print("Test " + str(i + 1) + " runtime: " + str(t/testRuns))