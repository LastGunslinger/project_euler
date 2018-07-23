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
	divisors = {x for x in range(1, num) if num % x == 0}
	return sum(divisors) > num

def find_abundant_nums(limit):
	return {x for x in range(12, limit + 1) if is_abundant(x)}

def sums_of_abundants(abundant_nums, limit):
	return {x + y for x in abundant_nums for y in abundant_nums if x <= y and x + y <= limit}

def remove_abundant_sums(abundant_sums, limit):
	return [x for x in range(1, limit + 1) if x not in abundant_sums]

def solve():
	limit = 28123
	abnums = find_abundant_nums(math.ceil(limit))
	abnum_sums = sums_of_abundants(abnums, limit)
	result = remove_abundant_sums(abnum_sums, limit)
	print(result)
	return sum(result)

def test_main():
	limit = 120
	assert is_abundant(28) == False
	test_abnums = find_abundant_nums(limit)
	assert test_abnums == {12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120}
	test_sums = sums_of_abundants(test_abnums, limit)
	assert len(test_sums) == len({x + y for x in test_abnums for y in test_abnums if x <= y and x + y <= 120})
	assert test_sums == {x + y for x in test_abnums for y in test_abnums if x <= y and x + y <= 120}
	# print(test_sums)
	# test_non_abnums = remove_abundant_sums(test_sums, limit)
	# print(f'{test_non_abnums} - {len(test_non_abnums)}')

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))