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

def main(limit):
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
	main(15)

if __name__ == '__main__':
	start = time.time()
	print(main(1000))
	print('--- {} seconds ---'.format(time.time()-start))