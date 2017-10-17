import itertools
import math

"""
By using a nifty method of checking divisibility by three, we can ignore 
the order of digits in a proposed solution which reduces our search space by a ton.
By starting with the longest possible solutions and working down, as soon as a multiple 
of three is found we can stop searching for any numbers of lesser length.
"""

def divisibleByThree(n):
	while(int(math.log10(n))+1 > 1):
		digitalSum = 0
		for i in str(n):
			digitalSum +=int(i)
		n = digitalSum
	return n % 3 == 0

def answer(L):
	L= list(map(str, L))
	for i in range(9, 0, -1):
		combinations = map(list, itertools.combinations(L, i))

		for n in combinations:
			n.sort(reverse=True)
		combinations.sort(reverse=True)

		for n in combinations:
			if(divisibleByThree(int(''.join(n)))):
				return int(''.join(n))
	return 0


print(answer([3, 1, 4, 1, 8, 2, 3]))

"""
I sure do hope the plates are safe to eat from after all this sorting 
and handling, I wouldn't like it if any bunny got sick under my watch
"""