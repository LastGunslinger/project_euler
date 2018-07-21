'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

def solve():
	largest_palindrome = 0
	# loop backwards through n * m for 100 <= m <= n <= 1000
	for m in reversed(range(100, 1000)):
		for n in reversed(range(100, 1000)):
			product = m * n
			if str(product) == str(product)[-1::-1] and product > largest_palindrome:
				largest_palindrome = product
	return largest_palindrome

if __name__ == '__main__':
	print(main())