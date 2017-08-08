'''

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''
import time
import pytest
import math

def sum_divisors(num):
	divisors = [1]
	for x in range(2, math.ceil(math.sqrt(num))):
		if num % x == 0:
			divisors.append(x)
			divisors.append(int(num/x))
	return sum(divisors)

def main():
	amicables = find_amicables(10000)
	return sum([x for (x, y) in amicables])

def find_amicables(ubound):
	all_sums = []
	amicables = []
	for x in range(2, ubound):
		sum_of_divisors = sum_divisors(x)
		all_sums.append((x, sum_of_divisors))
		if (sum_of_divisors, x) in all_sums and x != sum_of_divisors:
			print(f'{x}: {sum_of_divisors} -> {sum_of_divisors}: {x}')
			amicables.append((x, sum_of_divisors))
			amicables.append((sum_of_divisors, x)) 

	return amicables

def test_main():
	fd = sum_divisors(220)
	assert fd == 284
	fd = sum_divisors(284)
	assert fd == 220

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))