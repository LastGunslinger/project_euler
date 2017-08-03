'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
import time

def main():

	return sieve_of_Eratosthenes(2000000)

	primes = [2]
	current_num = 1
	while primes[-1] < 2000000:
		print(primes[-1])
		current_num += 2
		x = 0
		isPrime = True
		#while x < len(primes):
		while primes[x] < current_num/2:
			if current_num % primes[x] == 0:
				isPrime = False
				break
			x += 1
		if isPrime:
			primes.append(current_num)
	#print(primes)
	return sum([x for x in primes if x < 2000000])

def sieve_of_Eratosthenes(limit):
	primes = [x for x in range(2, limit)]
	prime_flags = [None for x in range(2, limit)]
	
	index = 0
	while None in prime_flags:
		if prime_flags[index] is not None:
			if is_prime(primes[index]):
				prime_flags[index] = True
				for flag in range(index, len(primes), index + 1):
					prime_flags[flag] = False
			else:
				prime_flags[index] = False
		index += 1

	print(primes)

def is_prime(num):
	x = 2
	while x < num / 2:
		if x % num == 0:
			return False
		x += 1
	return True


if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))