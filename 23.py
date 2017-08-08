'''

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

'''
import time
import pytest
import math

def is_abundant(num):
	divisors = [1]
	for x in range(2, math.ceil(math.sqrt(num))):
		if num % x == 0:
			divisors.append(x)
			divisors.append(int(num/x))
	return sum(divisors) > num

def find_all_abundant(limit):
	abundant_nums = []
	for x in range(2, limit + 1):
		if is_abundant(x):
			abundant_nums.append(x)
	return abundant_nums

def main():
	limit = 28123
	abundant_nums = find_all_abundant(limit)
	num_range = [x for x in range(1, limit + 1)]
	for abundant in abundant_nums:
		for other in abundant_nums:
			if abundant + other in num_range:
				num_range.remove(abundant + other)
	print(num_range)
	return sum(num_range)

def test_main():
	assert is_abundant(28) == False
	print(find_all_abundant(50))

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))