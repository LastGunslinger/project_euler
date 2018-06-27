'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''
from itertools import count
from primes import PrimeIterator
import time

def main(limit):
	for index, prime in enumerate(PrimeIterator()):
		print(f'{index:05}: {prime}')
		if index == limit - 1:
			return prime

if __name__ == '__main__':
	start = time.time()
	print(main(10001))
	print('--- {} seconds ---'.format(time.time()-start))