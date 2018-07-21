'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
from functools import reduce

def solve():
	primes = [2, 3, 5, 7, 11, 13, 17, 19] # all prime numbers <= 20
	prime_prod = reduce((lambda x, y: x * y), primes)

	result = prime_prod
	while True:
		if False in [ result % x == 0 for x in reversed(range(1, 21)) ]:
			result += prime_prod
		else:
			return result

if __name__ == '__main__':
	print(main())