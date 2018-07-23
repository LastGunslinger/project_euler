'''

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

'''
import time
import re
import pytest

def solve():
	data = '''
		75
		95 64
		17 47 82
		18 35 87 10
		20 04 82 47 65
		19 01 23 75 03 34
		88 02 77 73 07 63 67
		99 65 04 28 06 16 70 92
		41 41 26 56 83 40 80 70 33
		41 48 72 33 47 32 37 16 94 29
		53 71 44 65 25 43 91 52 97 51 14
		70 11 33 28 77 73 17 78 39 68 17 57
		91 71 52 38 17 14 91 43 58 50 27 29 48
		63 66 04 68 89 53 67 30 73 16 69 87 40 31
		04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
		'''
	data = data.split()
	data = [int(x) for x in data]
	triangle = gen_triangle(data)
	return max_sum(triangle)

def max_sum(triangle):
	
	for index in range(len(triangle) -2, -1, -1):
		for col in range(0, len(triangle[index])):
			left_branch = triangle[index + 1][col]
			right_branch = triangle[index + 1][col + 1]
			if left_branch >= right_branch:
				triangle[index][col] += left_branch
			else:
				triangle[index][col] += right_branch
			#triangle[index][col] += triangle[index + 1][col] if triangle[index + 1][col] > triangle[index + 1][col + 1] else triangle[index + 1][col + 1]
		print(triangle[-2])
		triangle.pop()

	return triangle[0][0]


def gen_triangle(data):
	triangle = []
	start = 0
	row_len = 1
	while start + row_len < len(data) + 1:
		triangle.append(data[start:start + row_len])
		start += row_len
		row_len += 1
	
	for row in triangle:
		print(row)

	return triangle

def test_max_triangle_sum():
	test_data = [ 3, 7 , 4, 2, 4, 6, 8, 5, 9, 3 ]
	test_data = gen_triangle(test_data)
	assert max_sum(test_data) == 23

if __name__ == '__main__':
	start = time.time()
	test_max_triangle_sum()
	print(main())
	print('--- {} seconds ---'.format(time.time()-start))