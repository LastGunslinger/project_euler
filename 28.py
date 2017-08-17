'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''
import time
import pytest

def create_matrix(rows, columns):
	return [ [0 for _ in range(columns)] for _ in range(rows) ]

def test_create_matrix():
	matrix = create_matrix(10, 10)
	for row in matrix:
		print(row)

def main():
	return

def test_main():
	pass

if __name__ == '__main__':
	start = time.time()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))