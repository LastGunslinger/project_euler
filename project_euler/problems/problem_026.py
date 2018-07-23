'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	 = 	0.5
1/3	 = 	0.(3)
1/4	 = 	0.25
1/5	 = 	0.2
1/6	 = 	0.1(6)
1/7	 = 	0.(142857)
1/8	 = 	0.125
1/9	 = 	0.(1)
1/10 = 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
import time
import pytest
import re
import math

def is_prime(number):
	if 1 < number <= 3:
		return True
	for x in range(2, math.ceil(math.sqrt(number) + 1 )):
		if number % x == 0:
			return False
	return True

def largest_prime(limit):
	prime = 2
	for divisor in range(2, limit):
		if is_prime(divisor):
			prime = divisor
	return prime

def find_repeat_length(divisor):
	'''
	Let n < d, and you're trying to figure out the repeating part of n/d. Let p be the number of digits in the repeating part: then n/d = R * 10^(-p) + R * 10^(-2p) + ... = R * ((10^-p)^1 + (10^-p)^2 + ...). The bracketed part is a geometric series, equal to 1/(10^p - 1).
	So n / d = R / (10^p - 1). Rearrange to get R = n * (10^p - 1) / d. To find R, loop p from 1 to infinity, and stop as soon as d evenly divides n * (10^p - 1).
	'''
	dividend = 1 * 9
	new_dividend = dividend
	divisor = 2
	repeating_length = 1
	while new_dividend % divisor:
		new_dividend = new_dividend * 10 + dividend
		repeating_length += 1
	return repeating_length

def test_find_repeat_length():
	assert find_repeat_length(7) == 6
	assert find_repeat_length(263) == 262


def long_divide(dividend, divisor):
	pattern = re.compile(r'(\d+)\1{3,}', re.IGNORECASE)
	quotient = ''
	remainder = 1
	while remainder != 0 :
		quotient += str(int(dividend / divisor))
		if quotient == '0':
			quotient += '.'
		remainder = dividend % divisor
		dividend = remainder * 10
		match = pattern.search(quotient)
		if match and quotient[-1] != '0':
			quotient = re.sub(r'{}+'.format(match.group()), r'({})'.format(match.group(1)), quotient)
			# print(match.group(1))
			return quotient, len(match.group(1))
	return quotient, 0

def solve(limit):
	longest_recurring = 7
	recurring_length = 6
	for x in range(1, limit):
		q, length = long_divide(1, x)
		if length > recurring_length:
			recurring_length = length
			longest_recurring = x
			print(f'1 / {x} : {recurring_length}')
	return longest_recurring

def test_main():
	assert long_divide(1, 4) == ('0.25', 0)
	assert long_divide(1, 5) == ('0.2', 0)
	assert long_divide(1, 7) == ('0.(142857)', 6)
	main(50)

def test_is_prime():
	assert is_prime(43) == True
	assert is_prime(18) == False

def test_largest_prime():
	assert largest_prime(20) == 19
	print(largest_prime(1000))

if __name__ == '__main__':
	start = time.time()
	print(main(1000))
	print('--- {} seconds ---'.format(time.time()-start))