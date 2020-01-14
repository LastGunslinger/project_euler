prompt = '''

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''


class Matrix:
    def __init__(self, rows: int, columns: int) -> None:
        self.matrix = [[0 for _ in range(columns)] for _ in range(rows)]
        self.center = int(rows / 2), int(columns / 2)
        self.size = len(self.matrix)

    def get_coordinate(self, x: int, y: int) -> int:
        return self.matrix[x][y]

    def set_coordinate(self, x: int, y: int, value: int) -> None:
        self.matrix[x][y] = value

    def __repr__(self) -> str:
        print_str = ''
        for row in self.matrix:
            print_str += row.__repr__() + '\n'
        return print_str


def paint_box(matrix: Matrix) -> Matrix:
    box_size = 3
    count = 1
    x, y = matrix.center
    matrix.set_coordinate(x, y, count)
    while box_size <= matrix.size:
        y += 1
        count += 1
        matrix.set_coordinate(x, y, count)
        for _ in range(box_size - 2):
            x += 1
            count += 1
            matrix.set_coordinate(x, y, count)
        for _ in range(box_size - 1):
            y -= 1
            count += 1
            matrix.set_coordinate(x, y, count)
        for _ in range(box_size - 1):
            x -= 1
            count += 1
            matrix.set_coordinate(x, y, count)
        for _ in range(box_size - 1):
            y += 1
            count += 1
            matrix.set_coordinate(x, y, count)
        box_size += 2
    return matrix


def test_paint_box() -> None:
    logger.debug()
    matrix = Matrix(5, 5)
    logger.debug(paint_box(matrix))


def sum_diagonals(matrix: Matrix) -> int:
    diagonal = {matrix.matrix[x][y] for x in range(matrix.size) for y in range(
        matrix.size) if (x == y or x + y == matrix.size - 1)}
    return sum(diagonal)


def test_sum_diagonals() -> None:
    matrix = Matrix(5, 5)
    matrix = paint_box(matrix)
    logger.debug(sum_diagonals(matrix))


async def solve(logger) -> int:
    logger.debug(prompt)
    size = 1001
    mtx = Matrix(size, size)
    mtx = paint_box(mtx)
    return sum_diagonals(mtx)
