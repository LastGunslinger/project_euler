'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
import time
import math

def main():
	limit = 2000000
	return sieve_of_Reggie(limit)

	# return sieve_of_Eratosthenes(limit)

def sieve_of_Reggie(limit):
	primes = [x for x in range(2,limit)]
	primes = [primes[0]] + [primes[x] for x in range(1,len(primes), 2)]

	x = 1
	while x < len(primes):
		if isPrime(primes[x], primes):
			prime_number = primes[x]
			print(prime_number)
			index = x + 1
			while index < len(primes):
				#print(primes[index])
				if primes[index] % prime_number == 0:
					primes.remove(primes[index])
				else:
					index += 1
		x += 1
	return sum(primes)

def isPrime(number, primes):
	x = 0
	while primes[x] < math.sqrt(number):
		if number % primes[x] == 0:
			return False
		x += 1
	return True

def sieve_of_Eratosthenes(limit):
	primes = [x for x in range(2, limit)]
	prime_flags = [None for x in primes]
	prime_flags[0] = True
	for x in range(2, len(prime_flags), 2):
		prime_flags[x] = False
	for x in range(3, len(prime_flags), 5):
		prime_flags[x] = False

	index = 1
	while None in prime_flags and index < len(primes):
		if prime_flags[index] is None:
			if is_prime(index, primes, prime_flags):
				print(primes[index])
				prime_flags[index] = True
				for flag in range(index + primes[index], len(primes), primes[index]):
					if prime_flags[flag] == None:
						prime_flags[flag] = False
			else:
				prime_flags[index] = False
		index += 2
	return sum([x[0] for x in zip(primes, prime_flags) if x[1]])

def is_prime(index, primes, prime_flags):
	x = 0

	while primes[x] < primes[index]/2:
		if prime_flags[x] and primes[index] % primes[x] == 0:
			return False
		x += 1
	return True


if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))