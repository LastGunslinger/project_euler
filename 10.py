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
	primes = [2, 3] + [x for x in range(5,limit, 2)]
	# print(primes)
	x = 1
	while x < len(primes):
		if isPrime(primes[x], primes):
			prime_number = primes[x]
			print(f'{prime_number} - {len(primes)} potential primes left')
			new_primes = primes[:x+1] + [ num for num in primes[x+1:] if num % prime_number != 0 ]
			if len(new_primes) == len(primes):
				break
			else:
				primes = new_primes
			# print(primes)
		x += 1
	print(primes)
	return sum(primes)

def isPrime(number, primes):
	x = 1
	while primes[x] <= math.sqrt(number):
		if number % primes[x] == 0:
			return False
		x += 1
	return True

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))