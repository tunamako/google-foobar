from collections import Counter

#This challenge seemed impossibly hard until i mapped out the process of finding preimages
#on paper, which showed me the trick to the problem: the preimage (composed of two rows) for a given row
#in the input graph is valid if its top row is identical to the bottom row of a preimage for the previous 
#row in the input graph. It might sound like a mouthful but it'll get our lost bunnies safe and sound!


#The possible preimages for each cell state, 0 and 1
preImageBoxes = {
	0: [	
		((0, 0), (0, 0)),
		((0, 0), (1, 1)),
		((0, 1), (0, 1)),
		((0, 1), (1, 0)),
		((0, 1), (1, 1)),
		((1, 0), (0, 1)),
		((1, 0), (1, 0)),
		((1, 0), (1, 1)),
		((1, 1), (0, 0)),
		((1, 1), (0, 1)),
		((1, 1), (1, 0)),
		((1, 1), (1, 1))
	],
	1: [
		((0, 0), (0, 1)),
		((0, 0), (1, 0)),
		((0, 1), (0, 0)),
		((1, 0), (0, 0))
	]

}

def generatePreimages(row, bottomRows):
	preimages, stack, maxImageLen, bottomRowLen = [], [], len(row) + 1, len(bottomRows)

	#add all starting configurations to stack
	for box in preImageBoxes[row[0]]:
		stack.append([list(box[0]), list(box[1])])

	while len(stack) > 0:
		image = stack.pop()
		imageLen = len(image[0])

		#if image is complete and valid, format and add it to preimages
		if imageLen == maxImageLen:
			image = [tuple(image[0]),  tuple(image[1])]
			if image[0] in bottomRows or bottomRowLen == 0:
				preimages.append(image)
			continue

		#get next values to extend preimage 
		for box in preImageBoxes[row[imageLen - 1]]:
			topLeft, topRight = box[0][0], box[0][1],
			bottomLeft, bottomRight = box[1][0], box[1][1]

			if topLeft== image[0][-1] and bottomLeft == image[1][-1]:
				extendedImage = [image[0] + [topRight], image[1] + [bottomRight]]
				stack.append(extendedImage)
	return preimages


def answer(graph):
	if len(graph) < len(graph[0]):
		graph = list(zip(*graph[::-1])) #rotate 90 degrees

	bottomRows = Counter()
	for image in generatePreimages(graph[0], bottomRows):
		bottomRows[image[1]] += 1

	for row in graph[1:]:
		nextBottomRows = Counter()

		for image in generatePreimages(row, bottomRows):
	 		nextBottomRows[image[1]] += bottomRows[image[0]]

		bottomRows = nextBottomRows

	return sum(bottomRows.itervalues())
"""
tests = [
	[
		[True, False],
		[False, False]
	],
	[
		[True, False, True], 
		[False, True, False], 
		[True, False, True]
	],
	[
		[True, False, True, False, False, True, True, True],
		[True, False, True, False, False, False, True, False],
		[True, True, True, False, False, False, True, False],
		[True, False, True, False, False, False, True, False],
		[True, False, True, False, False, True, True, True]
	],
	[
		[True, True, False, True, False, True, False, True, True, False], 
		[True, True, False, False, False, False, True, True, True, False], 
		[True, True, False, False, False, False, False, False, False, True], 
		[False, True, False, False, False, False, True, True, False, False]
	],
	[
		[False, True, True, False, False, False, False, True, False],
		[False, True, False, False, True, True, False, False, False],
		[False, True, True, True, False, True, False, True, False],
		[False, True, True, False, False, True, True, True, True],
		[False, False, False, False, False, False, True, True, True],
		[False, True, True, True, False, False, True, False, False],
		[False, False, True, True, False, False, False, False, False],
		[False, False, True, True, False, False, False, False, False],
		[False, False, False, True, True, False, True, True, True],
		[False, False, False, False, True, False, False, False, False],
		[False, False, True, True, False, True, False, True, False],
		[False, False, True, False, True, False, True, False, False],
		[False, True, False, False, True, True, False, True, False],
		[False, True, False, True, True, True, False, True, True],
		[False, True, False, False, False, False, False, True, True],
		[False, True, False, True, True, False, True, True, True],
		[False, False, False, False, True, True, True, False, True],
		[False, False, False, False, True, True, False, False, False],
		[False, False, False, False, False, True, False, True, True],
		[False, False, False, False, False, False, True, True, False],
		[False, True, True, True, True, True, True, False, True],
		[False, True, False, True, False, True, True, True, False],
		[False, True, False, False, True, False, False, True, False],
		[False, False, False, False, True, True, True, False, True],
		[False, False, False, True, True, False, True, False, True],
		[False, False, True, True, True, True, True, True, False],
		[False, True, False, True, False, True, False, False, True],
		[False, False, True, False, False, False, True, True, False],
		[False, True, True, True, True, True, True, False, True],
		[False, True, False, True, False, False, True, True, True],
		[False, False, True, True, False, True, True, True, True],
		[False, False, False, False, False, True, True, True, True],
		[False, True, True, True, True, False, True, False, False],
		[False, True, False, True, False, True, True, False, False],
		[False, False, True, True, True, True, True, False, False],
		[False, False, False, True, False, False, True, False, False],
		[False, False, True, True, False, True, True, False, False],
		[False, False, True, True, False, True, False, True, False],
		[False, True, False, True, True, True, False, True, False],
		[False, False, True, True, False, True, False, True, True],
		[False, True, True, True, False, True, True, True, False],
		[False, True, False, True, False, False, False, False, True],
		[False, True, True, False, False, True, True, False, False],
		[False, False, False, False, False, False, True, True, True],
		[False, True, False, True, False, False, True, False, True],
		[False, False, False, False, True, True, True, True, True],
		[False, True, False, False, True, True, True, True, False],
		[False, False, False, False, False, False, False, True, True],
		[False, False, False, True, False, True, False, True, False],
	],
]

results = [0 for x in range(len(tests))]
answers = [38, 4, 254, 11567, 0]
timingsSum = [0 for x in range(len(tests))]
testRuns = 1

for j in range(1, testRuns + 1):
	print("Testing round " + str(j))
	for i in range(len(tests)):
		start = time.time()
		results[i] = answer(tests[i])
		timingsSum[i] += time.time() - start

		
for i, t in enumerate(timingsSum):
	grade = "Passed" if results[i] == answers[i] else "Failed with " + str(results[i])
	print("Test " + str(i + 1) + ": " + grade +  " | Runtime: " + str(t/testRuns))
"""
