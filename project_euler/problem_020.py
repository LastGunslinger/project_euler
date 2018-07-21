'''

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''
import time
import pytest

def solve():
	return sum_digits( factorial(100) )

def factorial(num):
	result = 1
	for x in range(1, num + 1):
		result *= x
	return result

def sum_digits(num):
	num_str = str(num)
	result = 0
	for digit in num_str:
		result += int(digit)
	return result 

def test_main():
	assert factorial(10) == 3628800
	assert sum_digits(3628800) == 27


if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))