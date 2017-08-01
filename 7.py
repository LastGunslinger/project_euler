'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

def main():
	prime_count = 0
	num = 2
	while prime_count < 10001:
		if is_prime(num):
			prime_count += 1
		num += 1
	return num - 1

def is_prime(num):
	for x in range(2,num)
		if num % x == 0 :
			return False
	return True

if __name__ == '__main__':
	print(main())