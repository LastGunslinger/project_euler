'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''
import time
import pytest

def main():
	# Mathematically, only a 2-digit * 3-digit number can be pandigital.
	# This reduces the range of numbers I need to look for.
	
	# First, find all 2 digit non-repeating numbers with no zero
	two_digits = set()
	for x in range(10, 100):
		x_set = set([int(c) for c in str(x)])
		if len(x_set) == 2 and 0 not in x_set:
			two_digits.add(tuple(int(c) for c in str(x)))
			#print(x)

	# Next, find all 3 digit non-repeating numbers with no zero
	three_digits = set()
	for x in range(100, 1000):
		x_set = set([int(c) for c in str(x)])
		if len(x_set) == 3 and 0 not in x_set:
			three_digits.add(tuple(int(c) for c in str(x)))
			#print(x)

	# Loop through all combinations for multiplications
	pandigital_sum = 0
	for x in two_digits:
		for y in three_digits:
			if len(set(x + y)) == 5 :
				product = int(''.join([str(i) for i in x])) * int(''.join([str(i) for i in y]))
				product_tup = tuple([int(c) for c in str(product)])
				if len(set(x + y + product_tup)) == 9 and len(product_tup) == 4 and 0 not in product_tup:
					print(str(x) + ' * ' + str(y) + ' = ' + str(product))
					pandigital_sum += product

	return pandigital_sum

def test_main():
	pass

if __name__ == '__main__':
	start = time.time()
	print(f'Result: {main()}')
	print('--- {} seconds ---'.format(time.time()-start))