'''

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?

'''
import time
import math

def solve():
	lattice = (20 + 20, 20)

	return combination(*lattice)

def combination(n, k):
	return math.factorial(n)/(math.factorial(k)*math.factorial(n - k))



if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))