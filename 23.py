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

def find_abundant_nums(limit):
	abundant_nums = []
	for x in range(12, limit + 1):
		if is_abundant(x):
			abundant_nums.append(x)
	return abundant_nums

def remove_abundant_sums(abundant_nums, limit):
	all_nums = [x for x in range(1, limit + 1)]
	lower_bound = 0
	for num in all_nums:
		for abnum in [x for x in abundant_nums if x < num]:
			if num - abnum in abundant_nums:
				print(f'{num} removed')
				all_nums.remove(num)
				break
				# all_nums[all_nums.index(num)] = None
	return all_nums


	while abundant_nums[i] <= limit/2:
		x = i + 1
		while abundant_nums[i] + abundant_nums[x] <= limit:
			if abundant_nums[i] + abundant_nums[x] in all_nums:
				all_nums.remove(abundant_nums[i] + abundant_nums[x])
				print(len(all_nums))
			elif 2*abundant_nums[i] in all_nums:
				all_nums.remove(2*abundant_nums[i])
				print(len(all_nums))
			x += 1
		i += 1
	return all_nums

def main():
	limit = 28123
	data = find_abundant_nums(limit)
	result = remove_abundant_sums(data, limit)
	print(result)
	return sum(result)

def test_main():
	limit = 50
	assert is_abundant(28) == False
	test_abnums = find_abundant_nums(limit)
	print(test_abnums)
	test_non_abnums = remove_abundant_sums(test_abnums, limit)
	print(test_non_abnums)

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))