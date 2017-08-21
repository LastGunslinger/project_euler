'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import time
import pytest

def gen_powers(power):
	lower_bound = 2**power
	upper_bound = (9**power) * power + 1
	for num in range(lower_bound, upper_bound):
		if sum([int(x)**power for x in str(num)]) == num:
			print(num)
			yield num

def test_gen_powers():
	test_data = [x for x in gen_powers(4)]
	assert test_data == [1634, 8208, 9474]
	assert sum(test_data) == 19316

def main(power):
	return sum([x for x in gen_powers(power)])

def test_main():
	pass

if __name__ == '__main__':
	start = time.time()
	print(f'Result: {main(5)}')
	print('--- {} seconds ---'.format(time.time()-start))