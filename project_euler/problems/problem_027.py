import time
import pytest
import math

def quadratic(x, a, b):
	return sum([x**2, a*x, b])

def test_Quadratic():
	assert quadratic(3, -79, 1601) == 1373

def is_prime(number):
	if number < 2:
		return False
	elif number == 2:
		return True
	else:
		for x in range(2, math.ceil(math.sqrt(number) + 1 )):
			if number % x == 0:
				return False
		return True

def test_is_prime():
	assert is_prime(2) == True
	assert is_prime(3) == True
	assert is_prime(18) == False
	assert is_prime(27) == False

def solve(a_limit, b_limit):
	prime_count = 0
	coeffs = (None, None)
	for a in range(-a_limit + 1, a_limit):
		for b in range(-b_limit, b_limit + 1):
			x = 0
			q = quadratic(x, a, b)
			primes = []
			while( is_prime(q) ):
				primes.append(q)
				x += 1
				q = quadratic(x, a, b)
			if len(primes) > prime_count:
				prime_count = len(primes)
				coeffs = (a, b)
				print(f'x^2 + ({a})x + ({b}) = {primes}')
	return coeffs, prime_count

def test_main():
	coeffs, prime_count = main(10, 10)
	print(coeffs, prime_count)

if __name__ == '__main__':
	start = time.time()
	print(main(1000, 1000))
	print('--- {} seconds ---'.format(time.time()-start))