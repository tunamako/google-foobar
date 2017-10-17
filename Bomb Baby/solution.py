from fractions import *

#From the beginning, it's easy to notice that a solution exists if M and F have no 
#common divisors as we can subtract 1 from the larger number to bring it down to 1.
#Similarly, if one input is 0, it will be impossible to turn it into 1 (unless maybe
#you have the kind of resources Commander Lambda seems to have)

def answer(M, F):
	M, F, counter = int(M), int(F), 0

	if ( (abs(M - F) % gcd(M,F) == 0) and  not (gcd(M,F) == 1) ) or min(M, F) == 0:
		return "impossible"

	while not M == F == 1:
		if M < F:
			M, F = F, M

		#If the smaller is 1, we can subtract 1 from the larger until it also reaches one, incurring M - 1 generations
		#Otherwise we subtract F from M until M is lesser than F, incurring floor(M/F) generations
		if F == 1:
			counter += M - 1 
			M = 1
		else:
			counter += M//F
			M = M % F

	return counter

#I can't imagine how large this LAMBCHOP must be if we can fit up to 10^50 bombs
#throughout its inner workings