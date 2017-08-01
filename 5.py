'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

def main():
	primes = [2, 3, 5, 7, 11, 13, 17, 19]
	result = 1
	for x in primes:
		result *= x
	prime_prod = result
	while True:
		test = [ result % x == 0 for x in range(20, 1, -1) ]
		print(test)
		if False in test:
			result += prime_prod
		else:
			return result

if __name__ == '__main__':
	print(main())