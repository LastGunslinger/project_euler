'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''
import time

def main():
	primes = [2]
	current_num = 1
	while primes[-1] < 2000000:
		print(primes[-1])
		current_num += 2
		x = 0
		while x < len(primes):
			if current_num % primes[x] == 0:
				break
			x += 1
		if x == len(primes):
			primes.append(current_num)
	print(primes)
	return sum([x for x in primes if x < 2000000])

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))