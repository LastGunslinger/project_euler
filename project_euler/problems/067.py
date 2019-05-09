prompt = '''

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

'''
from pathlib import Path

from loguru import logger

from project_euler import DATA_DIR
from typing import List


def solve():
    logger.debug(prompt)
    with Path(DATA_DIR, 'problem_067.txt').open() as data_file:
        triangle_data = []
        for data in data_file.readlines():
            row = [int(x) for x in data.split()]
            triangle_data += row
    triangle = gen_triangle(triangle_data)
    return max_sum(triangle)


def max_sum(triangle: List[List[int]]) -> int:
    for index in range(len(triangle) - 2, -1, -1):
        for col in range(0, len(triangle[index])):
            left_branch = triangle[index + 1][col]
            right_branch = triangle[index + 1][col + 1]
            if left_branch >= right_branch:
                triangle[index][col] += left_branch
            else:
                triangle[index][col] += right_branch
        print(triangle[-2])
        triangle.pop()

    return triangle[0][0]


def gen_triangle(data: List[int]) -> List[List[int]]:
    triangle = []
    start = 0
    row_len = 1
    while start + row_len < len(data) + 1:
        triangle.append(data[start:start + row_len])
        start += row_len
        row_len += 1

    return triangle


if __name__ == '__main__':
    solve()
