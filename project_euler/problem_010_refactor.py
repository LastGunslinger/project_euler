'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
import time
import math
# import primes

def solve(limit):
	return sum(x for x in range(limit) if primes.is_prime(x))

def test_main():

	assert main(10) == 17

if __name__ == '__main__':
	start = time.time()
	print(main(2000000))
	print('--- {} seconds ---'.format(time.time()-start))