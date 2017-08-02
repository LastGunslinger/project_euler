'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def main():
	primes = [2]
	current_num = 2
	while len(primes) <= 10001:
		current_num += 1
		x = 0
		while x < len(primes):
			if current_num % primes[x] == 0:
				break
			x += 1
		if x == len(primes):
			primes.append(current_num)
	return primes[10000]

if __name__ == '__main__':
	print(main())