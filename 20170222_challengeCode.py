from math import *

def listeTuple(n):
	solutions = []
	sum = n * ( n + 1) / 2
	maxToReach = n

	a = trunc(int(n)/ 2)
	longb = 0

	while (a < maxToReach) :
		b = (sum - a)/(a + 1)
		if( b <= n and trunc(b) == b and a != b):
			longb = trunc(b)
			maxToReach = longb
			solutions.append([a,longb])
			solutions.append([longb,a])
		a += 1
	return solutions

n = 101

solutions = listeTuple(n)

print(len(solutions))
print(solutions)
